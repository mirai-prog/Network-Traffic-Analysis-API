from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    """
    Эндпоинт проверки работоспособности API.
    """
    return {"status": "ok"}

