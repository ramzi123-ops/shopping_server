# PythonAnywhere Web App Configuration Fix

## Current Status
✅ Django commands work in console (check, migrate, collectstatic)
❌ Web app shows empty logs and doesn't load
❌ DNS lookup still fails for ramez.pythonanywhere.com

## Root Cause
The PythonAnywhere web app configuration doesn't match your actual file structure.

## Step-by-Step Fix

### 1. Check Current Web App Configuration

1. **Go to PythonAnywhere Dashboard**
   - Login to https://www.pythonanywhere.com/
   - Click "Web" tab

2. **Current Configuration (from your info):**
   - Source code: `/home/ramez/shopping_server/shopping_server`
   - Working directory: `/home/ramez/`
   - Virtualenv: `/home/ramez/shopping_server/shopping_server/venv`
   - WSGI file: `/var/www/ramez_pythonanywhere_com_wsgi.py`

### 2. Fix WSGI Configuration

1. **Click on WSGI configuration file link**
2. **Replace ALL content with this:**

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

3. **Save the file**

### 3. Verify Static Files Configuration

**In Web tab, Static files section:**
- URL: `/static/`
- Directory: `/home/ramez/shopping_server/shopping_server/static/`

**If not set, add it:**
1. Click "Enter URL" and type: `/static/`
2. Click "Enter path" and type: `/home/ramez/shopping_server/shopping_server/static/`
3. Click checkmark to save

### 4. Check Virtual Environment

**Virtualenv section should show:**
```
/home/ramez/shopping_server/shopping_server/venv
```

**If different, update it:**
1. Click on the virtualenv path
2. Change to: `/home/ramez/shopping_server/shopping_server/venv`
3. Save

### 5. Reload Web App

1. **Click the green "Reload ramez.pythonanywhere.com" button**
2. **Wait for reload to complete** (should show "reloaded successfully")

### 6. Test the Web App

1. **Open new browser tab**
2. **Go to: `https://ramez.pythonanywhere.com/`**
   - Should show Django welcome page or your app
3. **Go to: `https://ramez.pythonanywhere.com/api/items/`**
   - Should show API response or DRF browsable API

### 7. Check Error Logs

**If still not working:**
1. In Web tab, click "Error log"
2. Look for recent error messages
3. Also check "Server log"

## Common Issues and Solutions

### Issue: "ImportError: No module named 'shopping_server'"
**Solution:** Check WSGI file paths are correct

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution:** 
1. Verify virtualenv path: `/home/ramez/shopping_server/shopping_server/venv`
2. Reinstall requirements in console:
   ```bash
   cd /home/ramez/shopping_server/shopping_server
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Issue: "Static files not loading"
**Solution:** 
1. Run collectstatic again:
   ```bash
   python manage.py collectstatic --noinput
   ```
2. Check static files configuration in Web tab

### Issue: "DisallowedHost" error
**Solution:** Check `settings_production.py` has correct ALLOWED_HOSTS:
```python
ALLOWED_HOSTS = ['ramez.pythonanywhere.com', 'localhost', '127.0.0.1']
```

## Alternative: Create New Web App

**If configuration is too messed up:**

1. **Delete current web app** (in Web tab)
2. **Create new web app:**
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.10
3. **Configure from scratch** using steps above

## Test Commands After Fix

**Run these in console to verify:**

```bash
cd /home/ramez/shopping_server/shopping_server
source venv/bin/activate

# Test WSGI application
python -c "from shopping_server.wsgi import application; print('WSGI OK')"

# Test production settings
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_server.settings_production'); import django; django.setup(); print('Settings OK')"

# Test API endpoint locally
python manage.py runserver
# Then test http://localhost:8000/api/items/ in browser
```

## Expected Results

✅ Web app loads without errors
✅ API endpoints return JSON data
✅ Error logs show no critical errors
✅ Flutter app can connect to ramez.pythonanywhere.com

After following these steps, your PythonAnywhere deployment should work correctly!