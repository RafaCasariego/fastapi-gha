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

# Solo ejecuta Uvicorn si se corre localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
