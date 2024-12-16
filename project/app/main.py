from fastapi import FastAPI
from app.routers import upload

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    """
    Эндпоинт проверки работоспособности API.
    """
    return {"status": "ok"}


app.include_router(upload.router, prefix="/files", tags=["File Operations"])

@app.get("/healthcheck")
def healthcheck():
    """
    Эндпоинт проверки работоспособности API.
    """
    return {"status": "ok"}

