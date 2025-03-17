# otus-final-project

# Реализация блока МОДЕЛЬ

заходим на VM

ssh -i /c/Users/dtravin/.ssh/otus-key-rsa -L 8888:localhost:8888 ubuntu@158.160.48.136

## собрать конфигурацию
в папке infra_deploy
terraform apply -auto-approve

## запустить mlflow

ssh -i /home/ubuntu/yc ubuntu@158.160.45.112

запустить файл

source setup.sh

сделать screen

mlflow server --backend-store-uri postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=verify-full --default-artifact-root s3://${S3_BUCKET}/artifacts -h 0.0.0.0 -p 8000

mlflow UI:

Вход в UI: 158.160.45.112:8000

## загрузка файлов на s3

Это с базовой VM

make upload-dags-to-airflow
make upload-src-to-bucket

## запуск airflow

ssh -i /home/ubuntu/yc ubuntu@xx.xxx.xxx.xxx

Вход в UI: ip_внешний
логин: test_admin
пароль: видно при заходи на VM

## разобрать конфигурацию
terraform destroy -auto-approve


## сборка виртуального окружения

sudo apt-get update
pip install --upgrade pip

python -m venv pyspark_venv && \
source pyspark_venv/bin/activate

pip install --upgrade pip

pip install venv-pack loguru pandas hyperopt mlflow argparse scipy numpy boto3 psycopg2-binary catboost tqdm

venv-pack -o btc_venv_pack2.tar.gz

hdfs dfs -copyFromLocal btc_venv_pack2.tar.gz s3a://cold-s3-bucket/venvs/

## открыть jupiter под окружением

sсreen
source pyspark_venv/bin/activate
pip install jupyter ipykernel
python -m ipykernel install --user --name=pyspark_venv --display-name "Python (myenv)"
jupyter notebook


deactivate


## копирования с s3 на s3

проверка содержимого

s3cmd --config=/home/ubuntu/.s3cfg ls s3://cold-s3-bucket

s3cmd cp \
    --config=/home/ubuntu/.s3cfg \
    --acl-public \
    s3://airflow-bucket-c8f0a7919d61cd4e/artifacts/ \
    s3://cold-s3-bucket/mlflow/ \
    --recursive

## проверка данных на s3

проверяем (только с прокси)

s3cmd --config=/home/ubuntu/.s3cfg ls s3://cold-s3-bucket

# Docker

Собрать контейнер
sudo docker build -t datravin/otus-repo:btc .

Проверить образы:
sudo docker images

логин на dockerhub
sudo docker login -u datravin

запушить в docker hub
sudo docker push datravin/otus-repo:btc

удалить образ
sudo docker rm -f 3c47ea150835
sudo docker rmi otus-test2
sudo docker rmi 3c47ea150835

удаление по тегу:
sudo docker rmi datravin/otus-repo:btc

запуск с заходом внутрь:
docker run --rm -it -p 8880:8880 --name my_test_cont datravin/otus-repo:btc bash

Сборка с прокидыванием переменных
docker build --build-arg S3_ACCESS_KEY=$S3_ACCESS_KEY -t datravin/otus-repo:exp .

посмотреть запущенные контейнеры
docker ps

ПОлучить токен
https://app.docker.com/settings/personal-access-tokens

# kuber

--смотрим сервисы
kubectl get services --output=wide
--смотрим что собралось
kubectl get nodes --output=wide
--смотрим что собралось
kubectl get podes --output=wide
kubectl get pods --output=wide


kind create cluster --config=cluster-config.yaml

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml


kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s


kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml


sudo vim /etc/hosts

прописать строку 127.0.0.1 btc.ai

ЗАПУСК:
curl http://test.ai/predict


Алтернатинвый способ захода:
Вызывает службу (service)

kubectl port-forward svc/clusterip-svc 8080:80

и с другого места

curl http://localhost:8080/predict

curl http://localhost:8080/metrics

Можем дергать ручки

# Grafana

Развернем сервис мониторинга titanic'a

```shell
kubectl apply -f btc_monitoring.yml
```
Возможно, понадобится

```shell
kubectl create namespace monitoring
```


Для сбора метрик развернем сервисный аккаунт
```shell
kubectl apply -f prom_rbac.yml
```

Теперь заходим на VM с прокидываением порта 3000

Для того, чтобы вывести в UI графану:

```shell
export POD_NAME=$(kubectl --namespace default get pod -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=monitoring" -oname)
  kubectl --namespace default port-forward $POD_NAME 3000
```

http://localhost:3000

Get Grafana 'admin' user

Для получения пароля:
```shell
kubectl --namespace default get secrets monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo
```


Мы внутри




# prometheus

Заходим на VM с пробросом порта 9090
```shell
 kubectl port-forward svc/prometheus-operated -n default 9090:9090
```
И также в браузере

http://localhost:9090


# uvicorn

на VM запускаем (сборка окружения)
source setup_libs.sh

uvicorn app:app --reload --port 8888

c другой git'а заходим и проверяем

curl http://localhost:8888/predict

все должно отработать

# cli

сделать файл исполняемым
sudo chmod +x login_process.sh
