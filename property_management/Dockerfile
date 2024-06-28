# Utiliza la imagen base de Python 3.10 slim
FROM python:3.10-slim

# Evitar buffering de la salida de Python para que los logs aparezcan en tiempo real
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt /app/

# Instalar las dependencias definidas en requirements.txt
RUN pip install -r requirements.txt

# Copiar todo el contenido del proyecto al directorio de trabajo en el contenedor
COPY . /app/

# Copiar el archivo start.sh al directorio de trabajo en el contenedor
COPY start.sh /app/

# Dar permisos de ejecución al archivo start.sh
RUN chmod +x /app/start.sh

# Ejecutar las migraciones de Django al momento de construir el contenedor
RUN python manage.py makemigrations
RUN python manage.py migrate

# Comando por defecto para ejecutar cuando el contenedor se inicie
CMD ["./start.sh"]