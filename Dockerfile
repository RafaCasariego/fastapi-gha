FROM public.ecr.aws/lambda/python:3.12

# Establecer el directorio de trabajo en Lambda
WORKDIR ${LAMBDA_TASK_ROOT}

# Copiar el código de la API
COPY . .

# Instalar dependencias dentro del directorio de ejecución de Lambda
RUN pip install --no-cache-dir -r requirements.txt -t "${LAMBDA_TASK_ROOT}"

# Especificar el punto de entrada para Lambda
CMD ["main.lambda_handler"]
