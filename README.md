# llm_metrics
Core Repository for Evaluating Prompts and their metrics

## Setup

```
git clone https://github.com/priyanshu-sharma/llm_metrics.git

cd llm_metrics/

bash setup.sh
```
### Other Component Setup

#### Postgres

Open a new Terminal and configure Postgres Database with: -

```
sudo -u postgres psql
```


This will open postgres prompt. Enter the following commands to configure the database user. and '\q' to quit the postgres prompt.


```
create user pd_admin with encrypted password 'password';

grant all privileges on database product_design to pd_admin;
```


#### Redis Server

Open a new Terminal and start Redis Server with: -

```
redis-server
```


#### Redis CLI

Open a new Terminal and start Redis CLI with: -

```
redis-cli
```

#### RabbitMQ Server

Open a new Terminal and start RabbitMQ Server with: -

```
rabbitmq-server
```

### Metrics Server

Open a new Terminal and install Metrics Server dependencies with: -

```
cd src/metrics_server/

bash entrypoint.sh
```

And start Metrics Server with: -

```
python manage.py runserver
```

#### Metrics Server Celery

Open a new Terminal and start Metrics Server Celery with: -

```
cd src/metrics_server/

celery -A server_config.celery.app worker -c 1 -l info
```

### Metrics UI

Open a new Terminal and install UI dependencies using: -

```
cd metrics_ui/

bash entrypoint.sh
```

And start the UI Server with: -

```
npm start
```