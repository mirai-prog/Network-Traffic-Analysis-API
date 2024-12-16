from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path

# Создаем роутер
router = APIRouter()

# Директория для сохранения файлов
UPLOAD_DIR = Path("data")
UPLOAD_DIR.mkdir(exist_ok=True)  # Убедимся, что папка существует

@router.post("/upload", summary="Загрузка PCAP-файлов")
async def upload_file(file: UploadFile = File(...)):
    """
    Эндпоинт для загрузки PCAP-файлов.
    """
    # 1. Проверка расширения файла
    if not file.filename.endswith(".pcap"):
        raise HTTPException(status_code=400, detail="Допустимы только файлы с расширением .pcap")

    # 2. Ограничение размера файла (например, до 10 МБ)
    MAX_FILE_SIZE_MB = 10
    content = await file.read()
    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail=f"Файл слишком большой (максимум {MAX_FILE_SIZE_MB} МБ).")

    # 3. Сохранение файла
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as f:
        f.write(content)

    # 4. Возврат информации о файле
    return {
        "filename": file.filename,
        "size": len(content),
        "path": str(file_path),
    }

