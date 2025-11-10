"""Pytest configuration and fixtures"""
import pytest
from app import create_app, db
from app.models import User, License


@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner"""
    return app.test_cli_runner()


@pytest.fixture
def sample_user(app):
    """Create a sample user for testing"""
    user = User(username='testuser')
    user.set_password('testpassword')
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def sample_license(app):
    """Create a sample license for testing"""
    license = License(
        license_key='TEST-LICENSE-KEY-123',
        is_active=True
    )
    db.session.add(license)
    db.session.commit()
    return license
