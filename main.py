from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, AWS Lambda!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Definir la función de entrada para AWS Lambda
handler = Mangum(app)

def lambda_handler(event, context):
    return handler(event, context)

# Solo ejecuta Uvicorn si se corre localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
