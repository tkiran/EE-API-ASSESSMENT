import os

# Debug mode
DEBUG = os.getenv('DEBUG', False)

# Secret key for secure sessions
SECRET_KEY = os.getenv('SECRET_KEY', 'my-secret-key')

# Database settings
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///my-database.db')

# API keys
API_KEY = os.getenv('API_KEY', 'my-api-key')

# Environment-specific variables
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
