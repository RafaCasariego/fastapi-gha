from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, GitHub Actions!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
