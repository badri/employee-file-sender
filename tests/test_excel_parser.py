"""Tests for Excel parser service"""
import pytest
from app.services.excel_parser import ExcelParserService


@pytest.mark.unit
class TestExcelParserService:
    """Test Excel parsing functionality"""

    def test_parse_excel_placeholder(self, app):
        """Test Excel parsing - placeholder"""
        with app.app_context():
            service = ExcelParserService()
            result = service.parse_excel('dummy.xlsx')
            assert isinstance(result, list)
            assert len(result) == 2

    def test_validate_columns_placeholder(self, app):
        """Test column validation - placeholder"""
        with app.app_context():
            service = ExcelParserService()
            is_valid, missing = service.validate_columns(None)
            assert is_valid == True
            assert missing == []

    def test_clean_phone_numbers_placeholder(self, app):
        """Test phone number cleaning - placeholder"""
        with app.app_context():
            service = ExcelParserService()
            result = service.clean_phone_numbers('1234567890')
            assert result == '1234567890'
