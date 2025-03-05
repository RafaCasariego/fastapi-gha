# Usa la imagen oficial de AWS Lambda para Python 3.12
FROM public.ecr.aws/lambda/python:3.12

# Copia el código dentro del directorio correcto de Lambda
COPY ./app ${LAMBDA_TASK_ROOT}

# Instala dependencias en el entorno correcto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t "${LAMBDA_TASK_ROOT}"

# Define la función de entrada para Lambda
CMD ["handler.lambda_handler"]
