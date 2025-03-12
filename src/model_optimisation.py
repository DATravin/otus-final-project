import pandas as pd
import numpy as np
import pickle

from hyperopt import fmin, tpe, hp, STATUS_OK, Trials, SparkTrials, Trials
import mlflow
from mlflow.tracking import MlflowClient

import os
from loguru import logger
from functools import partial
from argparse import ArgumentParser
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import roc_auc_score,fbeta_score,classification_report
from sklearn.metrics import log_loss,roc_curve,auc,average_precision_score,accuracy_score,r2_score

from catboost import CatBoostClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.inspection import permutation_importance


from pyspark.sql import SparkSession, DataFrame, functions as F
from pyspark.sql.types import IntegerType,LongType,DoubleType,StringType

from datetime import datetime, timedelta,timezone

import bit_functions
import config_btc
# import classes


cols_full = config_btc.cols_before_selection




def get_spark():

    spark = (
            SparkSession
            .builder
            .appName("OTUS")
            .getOrCreate()
            )
    return spark

def objective(params,pipeline,X_train, y_train):
    """
    Кросс-валидация с текущими гиперпараметрами

    :params: гиперпараметры
    :pipeline: модель
    :X_train: матрица признаков
    :y_train: вектор меток объектов
    :return: средняя точность на кросс-валидации
    """

    logger.info(f"params {params}")

    # задаём модели требуемые параметры
    pipeline.set_params(**params)

    ovr = OneVsRestClassifier(estimator=pipeline)
    cv=KFold(n_splits=3,shuffle=False)


    score=np.mean(cross_val_score(ovr, X_train, y_train, cv=cv,scoring = 'roc_auc_ovr_weighted'))
    cv_f1_w=np.mean(cross_val_score(ovr,  X_train, y_train, cv=cv,scoring = 'f1_weighted'))

    dct_metrics = {
        'auc': score,
        'f1': cv_f1_w,
        }

    with mlflow.start_run():
        mlflow.log_params(params)
        mlflow.log_metrics(dct_metrics)

    # возвращаем результаты, которые записываются в Trials()
    return   {'loss': -score, 'params': params, 'status': STATUS_OK, 'model': ovr}

search_space = {

                'n_estimators' : hp.choice(label='N_E',
                        options=np.arange(100, 1000,100, dtype=int)),

                'learning_rate' : hp.uniform(label='L_R',
                        low=0.01,
                        high=0.1),

                'l2_leaf_reg': hp.uniform(label='R_L',
                        low=1,
                        high=500),
                }


def main(input_path):

    spark = get_spark()


    row_sdf = spark.read.parquet(input_path)

    #data_set_4h = pd.read_parquet('test_dataset_4H.parquet', engine='pyarrow')

    data_set_4h = row_sdf.toPandas()

    data_set_4h['target_new_up'] = np.where(data_set_4h['target_new']==1,1,0)
    data_set_4h['target_new_dw'] = np.where(data_set_4h['target_new']==-1,1,0)

    logger.info(f"dataset size {data_set_4h.shape}")

    cols_up_new = bit_functions.permutaion_list(data_set_4h,'target_new_up',cols_full)

    cols_dw_new = bit_functions.permutaion_list(data_set_4h,'target_new_dw',cols_full)

    len_orig = len(cols_full)
    len_up = len(cols_up_new)
    len_dw = len(cols_dw_new)

    if len_orig==len_up and len_orig==len_dw:
        final_columns_list = cols_full
    elif len_orig==len_up:
        final_columns_list = len_dw
    elif len_orig==len_dw:
        final_columns_list = len_up
    else:
        final_columns_list = list(set(cols_up_new + cols_dw_new))

    logger.info(f"final number of features {len(final_columns_list)}")


    X = data_set_4h[(data_set_4h.ROWNUM>=300)&(data_set_4h.ROWNUM<8500)][final_columns_list].copy()
    y = data_set_4h[(data_set_4h.ROWNUM>=300)&(data_set_4h.ROWNUM<8500)].target_new

    mlflow.set_experiment('btc_forecast')

    # запускаем hyperopt
    trials = Trials()
    model =CatBoostClassifier(verbose=False)
    best = fmin(
            # функция для оптимизации
                fn=partial(objective, pipeline=model, X_train=X, y_train=y),
                #fn=objective(params,X_train, y_train)
            # пространство поиска гиперпараметров
                space=search_space,
            # алгоритм поиска
                algo=tpe.suggest,
            # число итераций
            # (можно ещё указать и время поиска)
                max_evals=2,
            # куда сохранять историю поиска
                trials=trials,
            # random state
                #rstate=np.random.RandomState(1),
            # progressbar
                show_progressbar=True
            )


    best_result = trials.results[np.argmin([r['loss'] for r in trials.results])]['loss']
    best_params = trials.results[np.argmin([r['loss'] for r in trials.results])]['params']

    print('готово')
    print(best_result)
    print(best_params)


    model_name = 'btc_forecast'

    #experiment_id = get_experiment_id(model_name)

    with mlflow.start_run() as run:


        model =CatBoostClassifier(verbose=False)
        model.set_params(**best_params)
        model_best = OneVsRestClassifier(estimator=model)
        model_best.fit(X,y)


        mlflow.sklearn.log_model(model_best, artifact_path="models", registered_model_name=model_name)

        # run_id = run.info.run_id

        mlflow.log_params(best_params)
        mlflow.log_metric('auc', -best_result)

        client = MlflowClient()
        model_versions = client.search_model_versions(filter_string=f"name = '{model_name}'")


        if len(model_versions)==1:
            cur_version = model_versions[0].version
            client.transition_model_version_stage(name=model_name, version=cur_version, stage="Production")
        else:
            cur_version = client.get_latest_versions(model_name, stages=["None"])
            client.transition_model_version_stage(name=model_name, version=cur_version, stage="Staging")


        mlflow.end_run()



if __name__ == "__main__":


    parser = ArgumentParser()
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    parser.add_argument("--mlflow", required=True, help="Mlflow uri")
    parser.add_argument("--aws_acc", required=True, help="AWS accses key")
    parser.add_argument("--aws_sec", required=True, help="AWS secret key")
    parser.add_argument("--bucket_art", required=True, help="S3 bucket name for artifacts")
    args = parser.parse_args()
    bucket_name = args.bucket
    mlflow_ip = args.mlflow
    aws_acc = args.aws_acc
    aws_sec = args.aws_sec

    os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'https://storage.yandexcloud.net'
    os.environ['MLFLOW_TRACKING_URI'] = f'http://{mlflow_ip}:8000'
    os.environ["AWS_ACCESS_KEY_ID"] = f'{aws_acc}'
    os.environ["AWS_SECRET_ACCESS_KEY"] = f'{aws_sec}'
    os.environ["S3_ENDPOINT_URL"] = 'https://storage.yandexcloud.net'
    os.environ["S3_BUCKET_NAME"] = args.bucket_art


    bucket_name = 'cold-s3-bucket'

    input_path = f"s3a://{bucket_name}/btc_prepaired_data.parquet"

    main(input_path)
