#!/usr/bin/env bash

echo "Starting backend django server"
until cd /home/forafekt/apps/src/server
do
    echo "Waiting for server volume..."
done

echo "Running manage.py migrate"
until ../manage.py migrate
do
    echo "Waiting for database to be ready..."
    sleep 2
done

echo "Create superuser"
until ../manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('testpilot', 'forafekt@gmail.com', 'Admin123')"

do
    echo "Waiting for superuser..."
    sleep 2
done

echo "Running manage.py collectstatic"
../manage.py collectstatic --noinput


until cd ..
do
    echo "Server Module..."
done
echo "Starting backend django server"
echo "Running manage.py gunicorn on port 8000"
gunicorn server.wsgi --bind :8000 --workers 4 --threads 4 --reload

