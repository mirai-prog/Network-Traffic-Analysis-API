from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path
from project.app.services.analysis_service import analyze_pcap


router = APIRouter()

UPLOAD_DIR = Path("data")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload", summary="Загрузка PCAP-файлов")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pcap"):
        raise HTTPException(status_code=400, detail="Допустимы только файлы с расширением .pcap")

    max_file_size_mb = 10
    content = await file.read()
    if len(content) > max_file_size_mb * 1024 * 1024:
        raise HTTPException(status_code=400, detail=f"Файл слишком большой (максимум {max_file_size_mb} МБ).")

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

    return {
        "total_packets": analysis_result["total_packets"],
        "protocols": analysis_result["protocols"],
        "ip_addresses": analysis_result["ip_addresses"],
        "http_requests": analysis_result["http_requests"],
        "dns_queries": analysis_result["dns_queries"],
    }
