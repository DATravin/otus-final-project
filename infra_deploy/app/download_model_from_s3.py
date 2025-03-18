
import os
import sys

import mlflow
import pandas as pd
import numpy as np
import pickle

from catboost import CatBoostClassifier
from sklearn.multiclass import OneVsRestClassifier
from dotenv import load_dotenv


def main():


    model_uri=f's3://{S3_BUCKET_NAME}/mlflow/1/047766d288bd4e9ebed191dc75012acd/artifacts/models/'

    loaded_model = mlflow.sklearn.load_model(model_uri)

    with open("model_best.pkl", "wb") as f:
        pickle.dump(loaded_model, f)

if __name__ == "__main__":

    load_dotenv()

    os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'https://storage.yandexcloud.net'
    os.environ["S3_ENDPOINT_URL"] = 'https://storage.yandexcloud.net'
    os.environ["AWS_ACCESS_KEY_ID"] = os.getenv('S3_ACCESS_KEY')
    os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv('S3_SECRET_KEY')
    os.environ["S3_BUCKET_NAME"] = os.getenv('S3_BUCKET_NAME')
    S3_BUCKET_NAME = bucket_name = 'cold-s3-bucket'


    main()
