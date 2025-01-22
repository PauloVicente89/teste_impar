#!/bin/bash
set -e

source ../../project/.env

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:8000