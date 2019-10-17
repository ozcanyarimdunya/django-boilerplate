#!/bin/bash

cmd="$@"

function postgres_ready(){
python << END
import sys
import psycopg2
import os

try:
    host = os.getenv('DB_HOST')
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "... Sleeping. Postgres is unavailable"
  sleep 1
done

>&2 echo "... Continuing. Postgres is up"
exec $cmd
