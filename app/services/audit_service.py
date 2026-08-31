from typing import Dict, Any, List
from app.repositories.audit_repository import AuditRepository

class AuditService:
    def __init__(self, audit_repo: AuditRepository = None):
        self.audit_repo = audit_repo or AuditRepository()

    def get_logs(self, action: str = None, username: str = None, status: str = None, page: int = 1, per_page: int = 25):
        return self.audit_repo.list_logs(action=action, username=username, status=status, page=page, per_page=per_page)

    def verify_chain_integrity(self) -> Dict[str, Any]:
        return self.audit_repo.verify_integrity()
