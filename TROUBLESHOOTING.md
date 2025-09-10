# PythonAnywhere Deployment Troubleshooting

## Issue: "Something went wrong" with empty logs

This usually indicates a WSGI configuration problem. Follow these steps:

### Step 1: Check WSGI Configuration

1. **Go to PythonAnywhere Web tab**
2. **Click on your WSGI configuration file**
3. **Replace the entire content with:**

```python
# WSGI config for PythonAnywhere deployment
import os
import sys

# Add your project directory to the sys.path
path = '/home/ramez/shopping_server'
if path not in sys.path:
    sys.path.insert(0, path)

# Use production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_server.settings_production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 2: Verify File Structure

In your PythonAnywhere console, check:

```bash
ls -la /home/ramez/shopping_server/
# Should show: manage.py, shopping_server/, shopping_list/, etc.

ls -la /home/ramez/shopping_server/shopping_server/
# Should show: settings.py, settings_production.py, wsgi.py, etc.
```

### Step 3: Test Django Settings

```bash
cd /home/ramez/shopping_server
source venv/bin/activate
python manage.py check --settings=shopping_server.settings_production
```

### Step 4: Check Python Path

In PythonAnywhere console:

```bash
cd /home/ramez/shopping_server
source venv/bin/activate
python -c "import django; print(django.get_version())"
python -c "import shopping_server.settings_production; print('Settings loaded successfully')"
```

### Step 5: Common Fixes

1. **Virtual Environment Path**
   - In Web tab, set Virtualenv to: `/home/ramez/shopping_server/venv`

2. **Source Code Path**
   - In Web tab, set Source code to: `/home/ramez/shopping_server`

3. **Static Files**
   - URL: `/static/`
   - Directory: `/home/ramez/shopping_server/static/`

4. **Collect Static Files**
   ```bash
   cd /home/ramez/shopping_server
   source venv/bin/activate
   python manage.py collectstatic --settings=shopping_server.settings_production
   ```

### Step 6: Test Minimal WSGI

If still not working, try this minimal WSGI config:

```python
import os
import sys

path = '/home/ramez/shopping_server'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping_server.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 7: Check Dependencies

```bash
cd /home/ramez/shopping_server
source venv/bin/activate
pip list
# Ensure Django, djangorestframework, django-cors-headers are installed
```

### Step 8: Force Reload

1. **Save WSGI file**
2. **Click "Reload ramez.pythonanywhere.com"**
3. **Wait 30 seconds before testing**

### Alternative: Use Development Settings First

If production settings cause issues, temporarily use:

```python
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping_server.settings'
```

Then switch back to production settings once working.

### Getting More Debug Info

Add this to your WSGI file temporarily:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("Django loaded successfully")
except Exception as e:
    print(f"Error loading Django: {e}")
    raise
```

### Contact Support

If none of these work:
1. Check PythonAnywhere forums
2. Contact PythonAnywhere support with your username (ramez)
3. Provide the exact error message and WSGI configuration