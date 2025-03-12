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

## проверка данных на s3

проверяем (только с прокси)

s3cmd --config=/home/ubuntu/.s3cfg ls s3://cold-s3-bucket
