from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, AWS Lambda!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Para que la API sea compatible con AWS Lambda 
handler = Mangum(app)