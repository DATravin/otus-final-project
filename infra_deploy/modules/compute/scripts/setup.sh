#!/bin/bash

# мое

# Функция для логирования
function log() {
    sep="----------------------------------------------------------"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $sep " | tee -a $HOME/user_data_execution.log
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [INFO] $1" | tee -a $HOME/user_data_execution.log
}

# Устанавливаем yc CLI
log "Installing yc CLI"
export HOME="/home/ubuntu"
curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash

# Проверяем, что yc доступен
if command -v yc &> /dev/null; then
    log "yc CLI is now available"
    yc --version
else
    log "yc CLI is still not available. Adding it to PATH manually"
    export PATH="$PATH:$HOME/yandex-cloud/bin"
    yc --version
fi

chown ubuntu:ubuntu /home/ubuntu/.config/
chmod -R 755 /home/ubuntu/.config/

chown ubuntu:ubuntu /home/ubuntu/.config/yandex-cloud/
chmod -R 755 /home/ubuntu/.config/yandex-cloud/


# Настраиваем config для yc?
log "Configuring yc"
cat <<EOF > /home/ubuntu/.config/yandex-cloud/config.yaml
current: default
profiles:
  default:
    token: ${token}
    cloud-id: ${cloud_id}
    folder-id: ${folder_id}
    compute-default-zone: ${zone}
EOF

chown ubuntu:ubuntu /home/ubuntu/.config/yandex-cloud/config.yaml
chmod 755 /home/ubuntu/.config/yandex-cloud/config.yaml

# Устанавливаем переменные

log "add env variables"
echo "S3_ACCESS_KEY=${access_key}" >> /home/ubuntu/.bashrc
echo "S3_SECRET_KEY=${secret_key}" >> /home/ubuntu/.bashrc
echo "S3_BUCKET_NAME=${s3_bucket_name}" >> /home/ubuntu/.bashrc
echo "S3_ENDPOINT_URL=https://storage.yandexcloud.net/" >> /home/ubuntu/.bashrc
echo "K8S_CLUSTER_ID=${cluster_id}" >> /home/ubuntu/.bashrc
echo "DOCKER_HUB_TOKEN=${docker_token}" >> /home/ubuntu/.bashrc

log "exports"
export HOME="/home/ubuntu"

# Настраиваем s3cmd как прокинуть туда переменные?
log "Configuring s3cmd"
cat <<EOF > /home/ubuntu/.s3cfg
[default]
access_key = ${access_key}
secret_key = ${secret_key}
host_base = storage.yandexcloud.net
host_bucket = %(bucket)s.storage.yandexcloud.net
use_https = True
EOF

chown ubuntu:ubuntu /home/ubuntu/.s3cfg
chmod 600 /home/ubuntu/.s3cfg

# Создаем директорию для скриптов на прокси-машине
log "Creating scripts directory on proxy machine"
mkdir -p /home/ubuntu/app
mkdir -p /home/ubuntu/app_test
mkdir -p /home/ubuntu/kuber

chown ubuntu:ubuntu /home/ubuntu/app
chmod 777 /home/ubuntu/app

chown ubuntu:ubuntu /home/ubuntu/app_test
chmod 777 /home/ubuntu/app_test

chown ubuntu:ubuntu /home/ubuntu/kuber
chmod 777 /home/ubuntu/kuber


log "Configuring .env"
cat <<EOF > /home/ubuntu/app/.env
[default]
S3_ACCESS_KEY = ${access_key}
S3_SECRET_KEY = ${secret_key}
S3_BUCKET_NAME = ${s3_bucket_name}
S3_ENDPOINT_URL = https://storage.yandexcloud.net/
EOF

chown ubuntu:ubuntu /home/ubuntu/app/.env
chmod 777 /home/ubuntu/app/.env



log "Configuring .env2"
cat <<EOF > /home/ubuntu/app_test/.env
[default]
S3_ACCESS_KEY = ${access_key}
S3_SECRET_KEY = ${secret_key}
S3_BUCKET_NAME = ${s3_bucket_name}
S3_ENDPOINT_URL = https://storage.yandexcloud.net/
EOF

chown ubuntu:ubuntu /home/ubuntu/app_test/.env
chmod 777 /home/ubuntu/app_test/.env

log "installing kubectl"
sudo apt install -y  snapd
snap install kubectl --classic

# Устанавливаем библиотеки
# log "Installing libs"
# sudo apt-get update
# sudo apt-get -y install python3-pip
# sudo pip install pandas
# sudo pip install numpy
# sudo pip install sklearn
# sudo pip install mlflow
# sudo pip install argparse
# sudo pip install catboost
# sudo pip install boto3
# sudo pip install s3cmd
# sudo pip install loguru
# sudo pip install pydantic
# sudo pip install uvicorn
# sudo pip install fastapi
# sudo pip install python-dotenv





# log "building docker imagelog "building docker image""
# docker build -f ./app/Dockerfile -t datravin/otus-repo:btc ./app


# log "login on docker hub"
# TOKEN="${docker_token}"

# echo "$TOKEN" | docker login -u datravin --password-stdin

# log "push on docker hub"
# docker push datravin/otus-repo:btc

log "creating context"
yc managed-kubernetes cluster get-credentials ${cluster_id} --external

yc managed-kubernetes cluster start ${cluster_id}

chown ubuntu:ubuntu /home/ubuntu/.kube/
chmod -R 755 /home/ubuntu/.kube/

chown ubuntu:ubuntu /home/ubuntu/.config/yandex-cloud/logs/
chmod -R 755 /home/ubuntu/.config/yandex-cloud/logs/

# log "apply all yamls"
# kubectl apply -f ./kuber/deployment.yaml
# kubectl apply -f ./kuber/service.yaml


log "Setup completed successfully"
