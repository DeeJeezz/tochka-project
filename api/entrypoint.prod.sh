#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_DB_HOST $SQL_DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@" 
