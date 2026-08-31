from typing import List, Optional
import json
from sqlalchemy import desc
from app.models.audit import AuditLog, SecurityEvent
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.crypto import calculate_audit_chain_hash

class AuditRepository(BaseRepository):
    def __init__(self):
        super().__init__(AuditLog)

    def log_event(self, action: str, resource_type: str, username: str, user_id: str = None,
                  resource_id: str = None, ip_address: str = None, user_agent: str = None,
                  status: str = 'SUCCESS', details: dict = None) -> AuditLog:
        # Get latest block hash for chain integrity
        last_log = AuditLog.query.order_by(desc(AuditLog.created_at)).first()
        prev_hash = last_log.current_block_hash if last_log else '0'*64
        
        details_str = json.dumps(details or {}, sort_keys=True)
        import datetime
        now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
        current_hash = calculate_audit_chain_hash(prev_hash, now_iso, action, user_id or 'SYSTEM', details_str)
        
        audit_entry = AuditLog(
            user_id=user_id,
            username=username,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            ip_address=ip_address,
            user_agent=user_agent,
            status=status,
            details_json=details_str,
            previous_block_hash=prev_hash,
            current_block_hash=current_hash
        )
        db.session.add(audit_entry)
        db.session.commit()
        return audit_entry

    def list_logs(self, action: str = None, username: str = None, status: str = None, page: int = 1, per_page: int = 25):
        query = AuditLog.query
        if action:
            query = query.filter_by(action=action)
        if username:
            query = query.filter_by(username=username)
        if status:
            query = query.filter_by(status=status)
        pagination = query.order_by(desc(AuditLog.created_at)).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages
        }

    def verify_integrity(self, limit: int = 500) -> dict:
        logs = AuditLog.query.order_by(AuditLog.created_at.asc()).limit(limit).all()
        tampered_ids = []
        for i, log in enumerate(logs):
            expected_prev = logs[i-1].current_block_hash if i > 0 else '0'*64
            if log.previous_block_hash and log.previous_block_hash != expected_prev:
                tampered_ids.append(log.id)
        return {
            'total_inspected': len(logs),
            'tampered_count': len(tampered_ids),
            'is_valid': len(tampered_ids) == 0,
            'is_tamper_free': len(tampered_ids) == 0,
            'tampered_ids': tampered_ids
        }
