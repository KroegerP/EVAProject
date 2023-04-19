#!/bin/bash

POSTGRES_USER="evadb"
POSTGRES_PASSWORD="evadb100"
DATABASE_NAME="evadb"
MY_FILES="database/migrations/*.sql"

export PGPASSWORD=$POSTGRES_PASSWORD

psql -U postgres < database/deleteDB.sql

echo "MAKE SURE YOU HAVE POSTGRES INSTALLED AND CAN LOGIN AS "postgres""

psql -U postgres < database/createUser.sql

echo "Created user '$POSTGRES_USER' and database '$DATABASE_NAME'."

psql -U evadb < database/initdb.sql

echo "Database initialized!"