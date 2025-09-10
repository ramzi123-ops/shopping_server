# WSGI config for PythonAnywhere deployment
# Copy this content to /var/www/ramez_pythonanywhere_com_wsgi.py on PythonAnywhere

import os
import sys

# Add your project directory to the sys.path
# Based on PythonAnywhere config: Source code is /home/ramez/shopping_server/shopping_server
path = '/home/ramez/shopping_server/shopping_server'
if path not in sys.path:
    sys.path.insert(0, path)

# Also add the parent directory to ensure proper imports
parent_path = '/home/ramez/shopping_server'
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

# Add the root directory as well
root_path = '/home/ramez'
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Use production settings for PythonAnywhere
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_server.settings_production')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()