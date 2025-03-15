#!/bin/bash

source .bashrc


# Функция для логирования
function log() {
    sep="----------------------------------------------------------"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $sep " | tee -a $HOME/user_data_execution.log
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [INFO] $1" | tee -a $HOME/user_data_execution.log
}


log "building docker imagelog "building docker image""
docker build -f ./app/Dockerfile -t datravin/otus-repo:btc ./app



log "login on docker hub"
TOKEN="${docker_token}"

echo "$TOKEN" | docker login -u datravin --password-stdin

log "push on docker hub"
docker push datravin/otus-repo:btc

log "creating context"
yc managed-kubernetes cluster get-credentials ${cluster_id} --external

yc managed-kubernetes cluster start ${cluster_id}

log "apply all yamls"
kubectl apply -f ./kuber/deployment.yaml
kubectl apply -f ./kuber/service.yaml
