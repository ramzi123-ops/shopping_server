# WSGI config for PythonAnywhere deployment
# This file should be used in the PythonAnywhere web app configuration

import os
import sys

# Add your project directory to the sys.path
path = '/home/ramez/shopping_server'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping_server.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())