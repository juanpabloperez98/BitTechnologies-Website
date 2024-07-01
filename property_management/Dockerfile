# Usa la imagen base de Python
FROM python:3.10.6-slim

# Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo en el contenedor
WORKDIR /code

# Instalar dependencias de Python
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el código de la aplicación
COPY . /code/

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Puerto en el que se ejecutará la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
