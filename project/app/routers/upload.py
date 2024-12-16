from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path

router = APIRouter()

UPLOAD_DIR = Path("data")
UPLOAD_DIR.mkdir(exist_ok=True)  

@router.post("/upload", summary="Загрузка PCAP-файлов")
async def upload_file(file: UploadFile = File(...)):
    """
    Эндпоинт для загрузки PCAP-файлов.
    """
    if not file.filename.endswith(".pcap"):
        raise HTTPException(status_code=400, detail="Допустимы только файлы с расширением .pcap")

    MAX_FILE_SIZE_MB = 10
    content = await file.read()
    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail=f"Файл слишком большой (максимум {MAX_FILE_SIZE_MB} МБ).")

    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as f:
        f.write(content)

    return {
        "filename": file.filename,
        "size": len(content),
        "path": str(file_path),
    }

