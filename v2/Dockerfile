# Usar imagen ligera de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de la aplicacion (app.py) desde el sistema host al contenedor
COPY app.py .

# Instalar el framework Flask, este es necesario para ejecutar la aplicacion web
RUN pip install flask

# Comando que se ejecuta al iniciar el contenedor para correr el script app.py
CMD ["python", "app.py"]