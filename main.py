from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root():
    return {"message": "¡Hola, AWS Lambda!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Función que AWS Lambda ejecutará
def lambda_handler(event, context):
    return handler(event, context)
