FROM public.ecr.aws/lambda/python:3.12

# Copiamos el código de la API al directorio correcto en Lambda
COPY ./ ${LAMBDA_TASK_ROOT}

# Instalamos dependencias dentro de la carpeta de ejecución de Lambda
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t "${LAMBDA_TASK_ROOT}"

# Especificamos el punto de entrada para Lambda
CMD ["app.handler"]
