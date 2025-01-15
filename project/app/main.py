import uvicorn
from fastapi import FastAPI
from routers import upload

app = FastAPI()

app.include_router(upload.router, prefix="/files", tags=["File Operations"])

@app.get("/healthcheck")
def healthcheck():
    """
    Эндпоинт проверки работоспособности API.
    """
    return {"status": "ok"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()