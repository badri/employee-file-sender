from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    """User model for authentication"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password against hash"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class License(db.Model):
    """License model for Keygen.sh integration"""
    __tablename__ = 'licenses'

    id = db.Column(db.Integer, primary_key=True)
    license_key = db.Column(db.String(255), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    expires_at = db.Column(db.DateTime, nullable=True)
    validated_at = db.Column(db.DateTime, nullable=True)
    metadata = db.Column(db.Text, nullable=True)  # Store JSON metadata from Keygen
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def is_valid(self):
        """Check if license is active and not expired"""
        if not self.is_active:
            return False
        if self.expires_at and self.expires_at < datetime.utcnow():
            return False
        return True

    def __repr__(self):
        return f'<License {self.license_key[:10]}... active={self.is_active}>'


class ProcessingLog(db.Model):
    """Log of file processing operations"""
    __tablename__ = 'processing_logs'

    id = db.Column(db.Integer, primary_key=True)
    excel_filename = db.Column(db.String(255), nullable=False)
    total_employees = db.Column(db.Integer, default=0)
    files_mapped = db.Column(db.Integer, default=0)
    messages_sent = db.Column(db.Integer, default=0)
    status = db.Column(db.String(50), default='pending')  # pending, processing, completed, failed
    error_message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<ProcessingLog {self.id} status={self.status}>'
