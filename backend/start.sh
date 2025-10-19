#!/bin/bash
echo "🚀 Starting Django backend on Railway..."
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn youtube_mp3_backend.wsgi:application --bind 0.0.0.0:$PORT
