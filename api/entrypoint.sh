#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_DB_HOST $SQL_DB_PORT; do
      sleep 0.1
      echo "Still waiting..."
    done

    echo "PostgreSQL started"
fi

export PYTHONPATH="/opt/tochka-api/:$PYTHONPATH"

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py loaddata common/fixtures/accounts.json

exec "$@" 
