#!/bin/sh

# Redis Setup
sudo apt-get update
sudo apt-get install redis-server nano vim pgcli curl
echo 'supervised systemd' >> /etc/redis/redis.conf
# redis-server

# RabbitMQ Setup
sudo apt-get install rabbitmq-server
# rabbitmq-server

# Postgres Setup
sudo apt-get install postgresql postgresql-contrib
# echo 'listen_addresses = "*"' >> /etc/postgresql/10/main/postgresql.conf
sudo service postgresql start
sudo -u postgres createdb metrics_api
# sudo service postgresql start
# sudo -u postgres psql
# create user pd_admin with encrypted password 'password';
# grant all privileges on database metrics_api to pd_admin;


# bash src/metrics_server/entrypoint.sh
# bash src/metrics_ui/entrypoint.sh