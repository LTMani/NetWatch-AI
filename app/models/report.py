from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from app.models.base import BaseModel, db

class GeneratedReport(BaseModel):
    """Exported executive or compliance reporting artifact."""
    __tablename__ = 'nw_generated_reports'

    title = Column(String(128), nullable=False)
    report_type = Column(String(32), default='DAILY_SUMMARY', nullable=False, index=True) # DAILY_SUMMARY, SECURITY_AUDIT, BANDWIDTH_USAGE, RISK_ASSESSMENT
    format = Column(String(16), default='HTML', nullable=False) # HTML, CSV, JSON, PDF
    
    file_path = Column(String(256), nullable=True)
    file_size_bytes = Column(Integer, default=0, nullable=False)
    generated_by = Column(String(64), default='system', nullable=False)
    summary_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
