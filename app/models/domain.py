from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text
from app.models.base import BaseModel, db

class DomainCategory(BaseModel):
    """Enterprise classification category for web traffic policy enforcement."""
    __tablename__ = 'nw_domain_categories'

    name = Column(String(64), unique=True, nullable=False, index=True)
    display_name = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    is_work_related = Column(Boolean, default=True, nullable=False)
    is_restricted = Column(Boolean, default=False, nullable=False)
    risk_weight = Column(Integer, default=10, nullable=False) # 0-100
    color_hex = Column(String(7), default='#64748B')

class DomainReputation(BaseModel):
    """Domain reputation cache and threat classification registry."""
    __tablename__ = 'nw_domain_reputations'

    domain = Column(String(256), unique=True, nullable=False, index=True)
    category = Column(String(64), default='Unknown', nullable=False, index=True)
    reputation_score = Column(Integer, default=80, nullable=False) # 0 (Malicious) to 100 (Trusted)
    is_malicious = Column(Boolean, default=False, nullable=False, index=True)
    is_suspicious = Column(Boolean, default=False, nullable=False)
    is_custom_override = Column(Boolean, default=False, nullable=False)
    threat_tags = Column(String(256), nullable=True) # e.g. 'phishing,dga,c2'
    query_count = Column(Integer, default=1, nullable=False)
    last_queried_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

class DomainFilterRule(BaseModel):
    """Administrative domain blocking or alerting policy rule."""
    __tablename__ = 'nw_domain_filter_rules'

    domain_pattern = Column(String(256), nullable=False, index=True) # e.g. '*.torrent.org', 'tiktok.com'
    category = Column(String(64), nullable=True)
    action = Column(String(32), default='BLOCK', nullable=False) # BLOCK, ALERT, THROTTLE
    is_enabled = Column(Boolean, default=True, nullable=False, index=True)
    reason = Column(String(256), nullable=False)
