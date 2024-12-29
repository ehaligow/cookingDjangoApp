#!/bin/sh
set -e

# Uruchomienie migracji
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Uruchomienie serwera
echo "Starting server..."
exec "$@"
