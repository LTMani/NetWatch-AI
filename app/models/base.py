import uuid
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_uuid() -> str:
    return str(uuid.uuid4())

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)

    def to_dict(self, exclude=None):
        exclude = set(exclude or [])
        result = {}
        for column in self.__table__.columns:
            if column.name in exclude:
                continue
            val = getattr(self, column.name)
            if isinstance(val, datetime):
                result[column.name] = val.replace(tzinfo=timezone.utc).isoformat()
            else:
                result[column.name] = val
        return result

    def update_from_dict(self, data, allowed_fields=None):
        allowed = set(allowed_fields) if allowed_fields else {c.name for c in self.__table__.columns if c.name not in ('id', 'created_at')}
        for key, value in data.items():
            if key in allowed and hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)
