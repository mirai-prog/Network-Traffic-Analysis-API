from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from pathlib import Path
from app.database import get_db
from app.models.analysis import PcapAnalysis
from app.services.pcap_analysis import analyze_pcap

router = APIRouter()
UPLOAD_DIR = Path("data")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/analyze", summary="Анализ PCAP-файла")
def analyze_uploaded_file(file_name: str, db: Session = Depends(get_db), filter_ip: str = None, filter_protocol: str = None, filter_port: int = None):
    file_path = UPLOAD_DIR / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Файл не найден.")

    try:
        analysis_result = analyze_pcap(str(file_path), filter_ip, filter_protocol, filter_port)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    db_analysis = PcapAnalysis(
        file_name=file_name,
        total_packets=analysis_result["total_packets"],
        protocols=analysis_result["protocols"],
        ip_addresses=analysis_result["ip_addresses"],
        http_requests=analysis_result["http_requests"],
        dns_queries=analysis_result["dns_queries"]
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)

    return analysis_result