#!/bin/bash
set -e

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

# uwsgi --http 0.0.0.0:8000 --master --enable-threads --module emploi.wsgi
uwsgi --ini emploi_uwsgi.ini