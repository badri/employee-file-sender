"""Tests for database models"""
import pytest
from datetime import datetime, timedelta
from app.models import User, License


@pytest.mark.unit
class TestUserModel:
    """Test User model"""

    def test_create_user(self, app):
        """Test user creation"""
        with app.app_context():
            user = User(username='newuser')
            user.set_password('password123')
            assert user.username == 'newuser'
            assert user.password_hash is not None

    def test_check_password(self, sample_user):
        """Test password verification"""
        assert sample_user.check_password('testpassword') == True
        assert sample_user.check_password('wrongpassword') == False


@pytest.mark.unit
class TestLicenseModel:
    """Test License model"""

    def test_create_license(self, app):
        """Test license creation"""
        with app.app_context():
            license = License(license_key='TEST-KEY')
            assert license.license_key == 'TEST-KEY'
            assert license.is_active == False

    def test_is_valid_active_license(self, sample_license):
        """Test valid active license"""
        assert sample_license.is_valid() == True

    def test_is_valid_expired_license(self, app):
        """Test expired license"""
        with app.app_context():
            from app import db
            license = License(
                license_key='EXPIRED-KEY',
                is_active=True,
                expires_at=datetime.utcnow() - timedelta(days=1)
            )
            db.session.add(license)
            db.session.commit()
            assert license.is_valid() == False
