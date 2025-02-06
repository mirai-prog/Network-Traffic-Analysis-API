import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload
from pathlib import Path

# Создаем экземпляр приложения FastAPI
app = FastAPI(
    title="PCAP Analysis API",
    description="API для загрузки, анализа и визуализации сетевого трафика из PCAP-файлов.",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Настраиваем базовую директорию для хранения данных
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Подключение маршрутов
app.include_router(upload.router, prefix="/api", tags=["Uploads"])

# Эндпоинт для проверки состояния приложения
@app.get("/healthcheck", tags=["Healthcheck"])
async def healthcheck():
    """
    Проверка состояния сервера.
    """
    return {"status": "ok", "message": "Server is running"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()