from typing import Optional, List
from sqlalchemy import or_
from app.models.user import User, Role, Permission, UserSession, ApiKey
from app.repositories.base_repository import BaseRepository
from app.models.base import db

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def get_by_username(self, username: str) -> Optional[User]:
        return self.model.query.filter_by(username=username, is_deleted=False).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.model.query.filter_by(email=email.lower(), is_deleted=False).first()

    def get_by_username_or_email(self, identifier: str) -> Optional[User]:
        ident = identifier.strip().lower()
        return self.model.query.filter(
            or_(self.model.username == identifier.strip(), self.model.email == ident),
            self.model.is_deleted == False
        ).first()

    def list_users(self, search: str = None, role: str = None, page: int = 1, per_page: int = 20):
        query = self.model.query.filter_by(is_deleted=False)
        if search:
            s = f'%{search.strip()}%'
            query = query.filter(or_(self.model.username.ilike(s), self.model.email.ilike(s), self.model.full_name.ilike(s)))
        if role:
            query = query.join(User.roles).filter(Role.name == role)
        pagination = query.order_by(User.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages
        }

    def get_role_by_name(self, name: str) -> Optional[Role]:
        return Role.query.filter_by(name=name, is_deleted=False).first()

    def list_roles(self) -> List[Role]:
        return Role.query.filter_by(is_deleted=False).all()

    def list_permissions(self) -> List[Permission]:
        return Permission.query.filter_by(is_deleted=False).all()

    def get_session_by_token_hash(self, token_hash: str) -> Optional[UserSession]:
        return UserSession.query.filter_by(session_token_hash=token_hash, is_revoked=False).first()

    def revoke_all_user_sessions(self, user_id: str):
        UserSession.query.filter_by(user_id=user_id, is_revoked=False).update({'is_revoked': True})
        db.session.commit()
