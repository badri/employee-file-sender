"""Tests for WhatsApp service"""
import pytest
from app.services.whatsapp import WhatsAppService


@pytest.mark.unit
class TestWhatsAppService:
    """Test WhatsApp message sending"""

    def test_send_message_placeholder(self, app):
        """Test message sending - placeholder"""
        with app.app_context():
            service = WhatsAppService()
            result = service.send_message('1234567890', 'Test message')
            assert result['success'] == True

    def test_send_document_placeholder(self, app):
        """Test document sending - placeholder"""
        with app.app_context():
            service = WhatsAppService()
            result = service.send_document('1234567890', '/path/to/doc.pdf')
            assert result['success'] == True

    def test_send_multiple_documents_placeholder(self, app):
        """Test multiple document sending - placeholder"""
        with app.app_context():
            service = WhatsAppService()
            result = service.send_multiple_documents('1234567890', ['/path/to/doc1.pdf'])
            assert isinstance(result, list)
