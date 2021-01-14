#!/bin/bash
source autodeploy_env.sh

PROD=${PRODUCTION:-false}

if [[ $DELETE_DB == true ]] || [[ $PROD == false ]] ; then
  rm db.sqlite3
  rm -rf */__pycache__
  if [[ $PROD == true ]] ; then
    python drop_db.py;
  fi;
fi;

./manage.py check

if [[ $STATIC == true ]] ; then
  python manage.py collectstatic --noinput
fi;

if [[ $MIGRATIONS == true ]] || [[ $PROD == false ]] ; then
  ./manage.py makemigrations
  ./manage.py migrate
fi;

if [[ $LOADDATA == true ]] || [[ $PROD == false ]] ; then
  ./manage.py loaddata user.json
fi;
