import pandas as pd
import numpy as np
import pickle

import warnings
warnings.filterwarnings("ignore")
import mlflow

import os
from loguru import logger
from functools import partial

from catboost import CatBoostClassifier
from sklearn.multiclass import OneVsRestClassifier

from datetime import datetime, timedelta,timezone

import bit_functions
import config_btc
import classes
from dotenv import load_dotenv

body5 = {
        "TimeKey":['2021-07-07T20:00:00Z'],
        "High":[34628.71],
        "Low":[33777.77],
        "Open":[34628.71],
        "Close":[33862.12],
        "Volume":[7923.75]

        }

load_dotenv()

os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'https://storage.yandexcloud.net'
os.environ["S3_ENDPOINT_URL"] = 'https://storage.yandexcloud.net'
os.environ["AWS_ACCESS_KEY_ID"] = os.getenv('S3_ACCESS_KEY')
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv('S3_SECRET_KEY')
os.environ["S3_BUCKET_NAME"] = os.getenv('S3_BUCKET_NAME')
S3_BUCKET_NAME = bucket_name = 'cold-s3-bucket'


def predict():


    model_uri=f's3://{S3_BUCKET_NAME}/mlflow/1/047766d288bd4e9ebed191dc75012acd/artifacts/models/'

    model_loc = mlflow.sklearn.load_model(model_uri)

    # with open('model_best.pkl','rb') as file:
    #     model_loc = pickle.load(file)

    logger.info(f"model upload")

    columns_models = []

    # Получение списка фичей
    features = model_loc.estimators_
    for idx, model in enumerate(features):
        columns_models = columns_models+model.feature_names_

    columns_models= list(set(columns_models))

    logger.info(f"features has been received")

    btcusdt_4h = pd.read_json('btcusdt_4h.json')

    base_df = btcusdt_4h[8300:8499]

    add_df = pd.DataFrame.from_dict(body5)

    full_df = pd.concat([base_df,add_df])


    agregate_4h_add=classes.Features(config_btc,'4H',bit_functions)._first_prep_no_d(full_df)

    data_set_4h_add=classes.Features(config_btc,'4H',bit_functions).transform(agregate_4h_add)

    x_loc2 = data_set_4h_add[columns_models].tail(1)

    logger.info(f"sample has been prepaired")

    verdict = model_loc.predict(x_loc2)[0]

    if verdict == -1:
        print('продовать')
        logger.info(f"sell")
        return 'sell'
    elif verdict ==0:
        print('чек')
        logger.info(f"pass")
        return 'pass'
    elif verdict == 1:
        print('покупать')
        logger.info(f"buy")
        return 'buy'
