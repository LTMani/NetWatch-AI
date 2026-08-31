from typing import List
from sqlalchemy import desc
from app.models.report import GeneratedReport
from app.models.base import db

class ReportRepository:
    def list_reports(self, limit: int = 20) -> List[GeneratedReport]:
        return GeneratedReport.query.order_by(desc(GeneratedReport.created_at)).limit(limit).all()

    def save_report(self, report: GeneratedReport) -> GeneratedReport:
        db.session.add(report)
        db.session.commit()
        return report
