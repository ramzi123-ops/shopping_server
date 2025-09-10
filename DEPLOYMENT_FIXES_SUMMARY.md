# PythonAnywhere Deployment Fixes Summary

## Issues Resolved

### 1. Duplicate Application Labels Error
**Problem:** `django.core.exceptions.ImproperlyConfigured: Application labels aren't unique, duplicates: rest_framework`

**Root Cause:** 
- `rest_framework` and `corsheaders` were already included in the base `settings.py` file
- `settings_production.py` was trying to add them again with `INSTALLED_APPS += [...]`
- Same issue with CORS middleware being added twice

**Fix Applied:**
- Removed duplicate entries from `settings_production.py`
- Added comments explaining that these are already in base settings

### 2. Port Already in Use Error
**Problem:** `Error: That port is already in use.`

**Solution:** Kill existing Django processes before starting new ones:
```bash
# Find and kill Django processes
pkill -f "python.*manage.py.*runserver"
# Or use a different port
python manage.py runserver 8001
```

## Files Modified

### 1. `settings_production.py`
**Changes:**
- Removed duplicate `'rest_framework'` and `'corsheaders'` from `INSTALLED_APPS`
- Removed duplicate CORS middleware configuration
- Kept CORS settings (origins, allow all) as these are production-specific

### 2. `test_production_settings.py` (New File)
**Purpose:** Test script to verify production configuration
**Features:**
- Tests Django setup with production settings
- Checks for duplicate applications
- Verifies WSGI application creation
- Tests API imports

## Next Steps for PythonAnywhere

### 1. Upload Fixed Files
```bash
# Upload the fixed settings_production.py to PythonAnywhere
# Upload test_production_settings.py for testing
```

### 2. Test Configuration
```bash
# On PythonAnywhere console:
cd /home/ramez/shopping_server/shopping_server
source venv/bin/activate
python test_production_settings.py
```

### 3. Test Django Setup
```bash
# Test production settings
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_server.settings_production'); import django; django.setup(); print('Settings OK')"

# Test WSGI
python -c "from shopping_server.wsgi import application; print('WSGI OK')"
```

### 4. Update Web App Configuration
1. Go to PythonAnywhere Web tab
2. Update WSGI file to use the fixed `wsgi_pythonanywhere_fixed.py`
3. Verify virtualenv path: `/home/ramez/shopping_server/shopping_server/venv`
4. Set static files: URL `/static/`, Directory `/home/ramez/shopping_server/shopping_server/static/`
5. Reload web app

### 5. Test API Endpoints
```bash
# Test locally first
python manage.py runserver 8001
# Then test: http://localhost:8001/api/items/

# Test on PythonAnywhere
# Visit: https://ramez.pythonanywhere.com/api/items/
```

## Expected Results

✅ **Production settings should load without errors**
✅ **No duplicate application labels**
✅ **WSGI application should initialize correctly**
✅ **API endpoints should be accessible**
✅ **Flutter app should connect successfully**

## Troubleshooting

If issues persist:

1. **Check PythonAnywhere error logs**
2. **Verify all file paths are correct**
3. **Ensure virtualenv has all dependencies**
4. **Test with the provided test script**
5. **Check ALLOWED_HOSTS includes your domain**

## Files Created/Modified

- ✅ `settings_production.py` - Fixed duplicate entries
- ✅ `test_production_settings.py` - New test script
- ✅ `wsgi_pythonanywhere_fixed.py` - Corrected WSGI configuration
- ✅ `WEBAPP_CONFIG_FIX.md` - Web app configuration guide
- ✅ `PYTHONANYWHERE_FIXES.md` - General troubleshooting guide

The main configuration issues have been resolved. Follow the next steps to complete the deployment.