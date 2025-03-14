#!/bin/bash


# Устанавливаем библиотеки
log "Installing libs"
sudo apt-get update
sudo apt-get -y install python3-pip
sudo pip install pandas
sudo pip install numpy
sudo pip install sklearn
sudo pip install mlflow
sudo pip install argparse
sudo pip install catboost
sudo pip install boto3
sudo pip install s3cmd
sudo pip install loguru
sudo pip install pydantic
sudo pip install uvicorn
sudo pip install fastapi
sudo pip install python-dotenv
sudo pip install tqdm


log "Setup completed successfully"
