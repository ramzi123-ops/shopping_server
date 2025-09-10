# Simple WSGI config for debugging PythonAnywhere deployment
# Use this if the main WSGI file doesn't work

import os
import sys

# Add your project directory to the sys.path
path = '/home/ramez/shopping_server'
if path not in sys.path:
    sys.path.insert(0, path)

# Also add the parent directory to ensure proper imports
parent_path = '/home/ramez'
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

# Use basic settings first for debugging
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping_server.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()