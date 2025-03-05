# Usamos una imagen oficial de Python ligera
FROM python:3.12-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos solo los archivos necesarios primero (para optimizar el cache)
COPY requirements.txt .

# Instalamos las dependencias sin usar la caché de pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código después
COPY . .

# Exponemos el puerto en el que correrá la API
EXPOSE 8000

# Comando para ejecutar la API con Lambda en producción
CMD ["handler.lambda_handler"]

