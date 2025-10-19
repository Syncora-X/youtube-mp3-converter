#!/bin/bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn youtube_mp3_backend.wsgi:application
