#!/bin/bash

# Esperar hasta que la base de datos esté lista
while ! nc -z db 5432; do
  echo "Esperando que la base de datos esté disponible..."
  sleep 1
done

# Ejecutar migraciones
python manage.py migrate

# Iniciar el servidor web
python manage.py runserver 0.0.0.0:8000