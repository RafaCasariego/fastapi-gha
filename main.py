from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, AWS Lambda!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Adaptar FastAPI para AWS Lambda
handler = Mangum(app)

# Solo ejecuta Uvicorn si se corre localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
