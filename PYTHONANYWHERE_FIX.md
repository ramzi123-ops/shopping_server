# PythonAnywhere Deployment Fix Guide

## Current Issues

1. **DNS Lookup Error**: `Failed host lookup: 'ramez.pythonanywhere.com'`
2. **Path Configuration**: Mismatch between WSGI paths and PythonAnywhere setup
3. **Web App Not Loading**: "Something went wrong" error

## Step-by-Step Fix

### 1. Fix WSGI Configuration

**Copy the content from `wsgi_pythonanywhere_fixed.py` to your PythonAnywhere WSGI file:**

1. Go to PythonAnywhere Web tab
2. Click on the WSGI configuration file: `/var/www/ramez_pythonanywhere_com_wsgi.py`
3. Replace ALL content with:

```python
# WSGI config for PythonAnywhere deployment
import os
import sys

# Add your project directory to the sys.path
path = '/home/ramez/shopping_server/shopping_server'
if path not in sys.path:
    sys.path.insert(0, path)

# Also add the parent directory
parent_path = '/home/ramez/shopping_server'
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

# Add root directory
root_path = '/home/ramez'
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Use production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_server.settings_production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 2. Verify PythonAnywhere Web App Configuration

**In PythonAnywhere Web tab, check these settings:**

- **Source code**: `/home/ramez/shopping_server/shopping_server`
- **Working directory**: `/home/ramez/`
- **Virtualenv**: `/home/ramez/shopping_server/shopping_server/venv`
- **WSGI file**: `/var/www/ramez_pythonanywhere_com_wsgi.py`

### 3. Fix Virtual Environment Path

**The virtualenv should be at the correct location:**

1. Open a Bash console on PythonAnywhere
2. Run these commands:

```bash
cd /home/ramez/shopping_server/shopping_server
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Test Django Configuration

**In PythonAnywhere console:**

```bash
cd /home/ramez/shopping_server/shopping_server
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=shopping_server.settings_production
python manage.py check
python manage.py migrate
python manage.py collectstatic --noinput
```

### 5. Reload Web App

1. Go to PythonAnywhere Web tab
2. Click the green "Reload" button
3. Wait for reload to complete

### 6. Test the API

**Try these URLs in your browser:**

- `https://ramez.pythonanywhere.com/` (should show Django page)
- `https://ramez.pythonanywhere.com/api/items/` (should show API response)

### 7. Check Error Logs

**If still not working:**

1. Go to PythonAnywhere Web tab
2. Click "Error log" link
3. Check for specific error messages
4. Also check "Server log" for more details

## Alternative Solutions

### If DNS Still Fails:

1. **Try HTTP instead of HTTPS** (temporary):
   ```dart
   static const String _baseUrl = 'http://ramez.pythonanywhere.com/api';
   ```

2. **Use IP address** (if available):
   - Find PythonAnywhere server IP
   - Use IP instead of domain name

3. **Check domain status**:
   - Verify ramez.pythonanywhere.com is active
   - Check if web app is enabled

### Common Issues:

1. **Web app not enabled**: Enable in Web tab
2. **Wrong Python version**: Use Python 3.10+
3. **Missing dependencies**: Reinstall requirements.txt
4. **Path issues**: Double-check all paths match exactly
5. **Settings module**: Ensure production settings are used

## Quick Test Commands

**Test Django import:**
```bash
cd /home/ramez/shopping_server/shopping_server
source venv/bin/activate
python -c "import django; print(django.get_version())"
```

**Test settings:**
```bash
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_server.settings_production'); import django; django.setup(); print('Settings OK')"
```

**Test WSGI:**
```bash
python -c "from shopping_server.wsgi import application; print('WSGI OK')"
```

After following these steps, your PythonAnywhere deployment should work correctly!