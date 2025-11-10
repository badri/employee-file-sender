from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, login_manager
from app.models import User, License

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    return User.query.get(int(user_id))


# ===== Authentication Routes =====

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page - placeholder"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        # TODO: Implement actual login logic
        flash('Login functionality coming soon', 'info')
        return redirect(url_for('auth.login'))

    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """Logout current user"""
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('auth.login'))


# ===== Main Application Routes =====

@main_bp.route('/')
def index():
    """Landing page - redirect to license or dashboard"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    # Check if license exists
    license = License.query.first()
    if not license or not license.is_valid():
        return redirect(url_for('main.license_activation'))

    return redirect(url_for('auth.login'))


@main_bp.route('/license')
def license_activation():
    """License activation page - placeholder"""
    return render_template('license.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard - placeholder"""
    return render_template('dashboard.html')


@main_bp.route('/upload')
@login_required
def upload():
    """File upload page - placeholder"""
    return render_template('upload.html')


@main_bp.route('/mapping')
@login_required
def mapping():
    """File mapping preview page - placeholder"""
    return render_template('mapping.html')


@main_bp.route('/send')
@login_required
def send():
    """Send messages page - placeholder"""
    return render_template('send.html')


@main_bp.route('/history')
@login_required
def history():
    """Processing history page - placeholder"""
    return render_template('history.html')
