from typing import List, Optional
from sqlalchemy import desc
from app.models.diagnostics import DiagnosticSession, DiagnosticStepResult
from app.repositories.base_repository import BaseRepository
from app.models.base import db

class DiagnosticsRepository(BaseRepository):
    def __init__(self):
        super().__init__(DiagnosticSession)

    def list_recent_sessions(self, limit: int = 10) -> List[DiagnosticSession]:
        return DiagnosticSession.query.order_by(desc(DiagnosticSession.timestamp)).limit(limit).all()

    def create_session(self, session: DiagnosticSession, steps: List[DiagnosticStepResult]) -> DiagnosticSession:
        db.session.add(session)
        db.session.flush()
        for step in steps:
            step.session_id = session.id
            db.session.add(step)
        db.session.commit()
        return session
