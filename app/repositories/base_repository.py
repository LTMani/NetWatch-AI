from typing import Any, Dict, List, Optional, Type, TypeVar
from sqlalchemy import desc, asc
from app.models.base import BaseModel, db

T = TypeVar('T', bound=BaseModel)

class BaseRepository:
    def __init__(self, model: Type[T]):
        self.model = model

    def get_by_id(self, entity_id: str, include_deleted: bool = False) -> Optional[T]:
        query = self.model.query.filter_by(id=entity_id)
        if not include_deleted and hasattr(self.model, 'is_deleted'):
            query = query.filter_by(is_deleted=False)
        return query.first()

    def get_all(self, include_deleted: bool = False, order_by_created_desc: bool = True) -> List[T]:
        query = self.model.query
        if not include_deleted and hasattr(self.model, 'is_deleted'):
            query = query.filter_by(is_deleted=False)
        if order_by_created_desc and hasattr(self.model, 'created_at'):
            query = query.order_by(desc(self.model.created_at))
        return query.all()

    def paginate(self, page: int = 1, per_page: int = 20, filters: Dict[str, Any] = None, include_deleted: bool = False):
        query = self.model.query
        if not include_deleted and hasattr(self.model, 'is_deleted'):
            query = query.filter_by(is_deleted=False)
        if filters:
            for key, val in filters.items():
                if hasattr(self.model, key) and val is not None:
                    query = query.filter(getattr(self.model, key) == val)
        if hasattr(self.model, 'created_at'):
            query = query.order_by(desc(self.model.created_at))
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages,
            'has_prev': pagination.has_prev,
            'has_next': pagination.has_next
        }

    def create(self, entity: T, commit: bool = True) -> T:
        db.session.add(entity)
        if commit:
            db.session.commit()
        return entity

    def update(self, entity: T, data: Dict[str, Any], commit: bool = True) -> T:
        entity.update_from_dict(data)
        if commit:
            db.session.commit()
        return entity

    def soft_delete(self, entity: T, commit: bool = True) -> T:
        if hasattr(entity, 'is_deleted'):
            entity.is_deleted = True
            if commit:
                db.session.commit()
        return entity

    def hard_delete(self, entity: T, commit: bool = True) -> None:
        db.session.delete(entity)
        if commit:
            db.session.commit()
