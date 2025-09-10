# Production settings for PythonAnywhere deployment
from .settings import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add your PythonAnywhere domain
ALLOWED_HOSTS = ['ramez.pythonanywhere.com', 'www.ramez.pythonanywhere.com']

# REST Framework and CORS headers are already included in base settings.py
# No need to add them again here

# CORS middleware is already included in base settings.py
# No need to add it again here

# CORS settings for Flutter app
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://ramez.pythonanywhere.com",
]

CORS_ALLOW_ALL_ORIGINS = True  # Only for development/testing

# REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# Static files configuration for production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Database configuration (using SQLite for simplicity)
# For production, consider using MySQL on PythonAnywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Generate a new secret key for production
# SECRET_KEY = 'your-production-secret-key-here'
# For now, using the development key (change this in production)