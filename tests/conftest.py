import pytest
from app import create_app
from app.models.base import db
from app.models.user import User, Role
from app.models.organization import Organization, Department, NetworkSite, Subnet
from app.utils.crypto import hash_password, generate_jwt_token

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        # Seed basic test fixture
        org = Organization(name='Test Org', domain='test.local')
        db.session.add(org)
        db.session.flush()

        role = Role(name='super_admin', display_name='Super Admin', is_system_role=True)
        db.session.add(role)
        db.session.flush()

        user = User(
            organization_id=org.id,
            username='testadmin',
            email='admin@test.local',
            password_hash=hash_password('Password123!'),
            full_name='Test Admin'
        )
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(app):
    with app.app_context():
        user = User.query.filter_by(username='testadmin').first()
        token = generate_jwt_token(user.id, user.email, 'super_admin')
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
