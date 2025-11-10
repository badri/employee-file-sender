# Employee File Sender

A Flask-based application for mapping employee files to Excel records and sending them via WhatsApp Business API.

## Features

- License management with Keygen.sh
- Single-user authentication
- Excel file parsing for employee data
- Automated file-to-employee mapping based on employee IDs
- WhatsApp Business API integration for document sending
- Processing history and logging
- Can be packaged as a desktop application using PyInstaller

## Tech Stack

- **Backend**: Python 3.11, Flask
- **Database**: SQLite
- **Frontend**: Tailwind CSS + DaisyUI
- **Testing**: pytest with TDD approach
- **Licensing**: Keygen.sh integration
- **Deployment**: Docker Compose (dev) / PyInstaller (desktop)

## Project Structure

```
employee-file-sender/
├── app/                    # Application package
│   ├── models.py          # Database models
│   ├── routes.py          # Flask routes
│   ├── services/          # Business logic services
│   └── templates/         # HTML templates
├── tests/                 # Test suite
├── config.py              # Configuration
├── docker-compose.yml     # Docker setup
├── requirements.txt       # Python dependencies
└── run.py                # Application entry point
```

## Getting Started

### Local Development with Docker

1. Clone the repository
2. Copy `.env.example` to `.env` and configure:
   ```bash
   cp .env.example .env
   ```

3. Start the application:
   ```bash
   docker-compose up --build
   ```

4. Access at `http://localhost:5000`

### Local Development without Docker

1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Run the application:
   ```bash
   flask run
   ```

## Testing

Run tests with pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test categories
pytest -m unit
pytest -m integration
```

## Building Desktop Application

Package the application using PyInstaller:

```bash
# TODO: Add PyInstaller configuration and build instructions
```

## Configuration

Key configuration variables in `.env`:

- `SECRET_KEY`: Flask secret key
- `KEYGEN_ACCOUNT_ID`: Your Keygen.sh account ID
- `KEYGEN_PRODUCT_ID`: Your product ID in Keygen
- `KEYGEN_API_TOKEN`: Keygen API token
- `WHATSAPP_API_TOKEN`: WhatsApp Business API token
- `WHATSAPP_PHONE_NUMBER_ID`: Your WhatsApp phone number ID

## Development Roadmap

- [ ] Implement actual license validation with Keygen.sh
- [ ] Complete Excel parsing logic
- [ ] Implement file-to-employee mapping algorithm
- [ ] Integrate WhatsApp Business API
- [ ] Add file upload handling
- [ ] Implement authentication flow
- [ ] Create PyInstaller build configuration
- [ ] Add comprehensive error handling
- [ ] Improve UI/UX with interactive components

## License

Proprietary - Licensed via Keygen.sh
