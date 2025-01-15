from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path
from app.services.analysis_service import analyze_pcap

router = APIRouter()

UPLOAD_DIR = Path("data")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload", summary="Загрузка PCAP-файлов")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pcap"):
        raise HTTPException(
            status_code=400, detail="Допустимы только файлы с расширением .pcap"
        )

    MAX_FILE_SIZE_MB = 10
    content = await file.read()
    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail=f"Файл слишком большой (максимум {MAX_FILE_SIZE_MB} МБ).",
        )

    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as f:
        f.write(content)

    return {
        "filename": file.filename,
        "size": len(content),
        "path": str(file_path),
    }


@router.post("/analyze", summary="Анализ PCAP-файла")
def analyze_uploaded_file(file_name: str):
    file_path = UPLOAD_DIR / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Файл не найден.")

    try:
        analysis_result = analyze_pcap(str(file_path))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return analysis_result
