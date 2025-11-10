"""Tests for Flask routes"""
import pytest


@pytest.mark.unit
class TestAuthRoutes:
    """Test authentication routes"""

    def test_login_page_loads(self, client):
        """Test login page is accessible"""
        response = client.get('/auth/login')
        assert response.status_code == 200
        assert b'Login' in response.data


@pytest.mark.unit
class TestMainRoutes:
    """Test main application routes"""

    def test_index_redirects_to_license(self, client):
        """Test index redirects when no license"""
        response = client.get('/')
        assert response.status_code == 302

    def test_license_page_loads(self, client):
        """Test license page is accessible"""
        response = client.get('/license')
        assert response.status_code == 200
        assert b'License' in response.data
