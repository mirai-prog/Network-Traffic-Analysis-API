from sqlalchemy import Column, Integer, String, JSON, DateTime, func
from app.database import Base

class PcapAnalysis(Base):
    __tablename__ = "pcap_analysis"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    total_packets = Column(Integer, nullable=False)
    protocols = Column(JSON, nullable=False)
    ip_addresses = Column(JSON, nullable=False)
    http_requests = Column(JSON, nullable=True)
    dns_queries = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())