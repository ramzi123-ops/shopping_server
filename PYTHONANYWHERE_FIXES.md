# PythonAnywhere Deployment Troubleshooting

## Issue: DNS Lookup Failed for ramez.pythonanywhere.com

The Flutter app is getting a DNS lookup error when trying to connect to `ramez.pythonanywhere.com`. This indicates the PythonAnywhere web app is not properly configured or activated.

## Root Cause Analysis

The error `Failed host lookup: 'ramez.pythonanywhere.com'` means:
1. The domain doesn't exist in DNS
2. The PythonAnywhere web app is not properly set up
3. The web app might be disabled or misconfigured

## Immediate Fix Steps

### Step 1: Check PythonAnywhere Web App Status

1. **Login to PythonAnywhere Dashboard**
   - Go to https://www.pythonanywhere.com/
   - Login with your account

2. **Check Web Tab**
   - Click on "Web" tab
   - Look for your web app configuration
   - **Status should be "Enabled" and green**

3. **Verify Domain Configuration**
   - Your web app should show: `ramez.pythonanywhere.com`
   - If it shows a different URL, note it down

### Step 2: Fix Web App Configuration

1. **If No Web App Exists:**
   ```
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.10
   - Set domain as: ramez.pythonanywhere.com
   ```

2. **Configure WSGI File:**
   - In Web tab, find "Code" section
   - Click on WSGI configuration file
   - Copy content from `wsgi_pythonanywhere.py`
   - Save the file

3. **Set Virtual Environment:**
   ```
   /home/ramez/shopping_server/venv
   ```

4. **Configure Static Files:**
   - URL: `/static/`
   - Directory: `/home/ramez/shopping_server/static/`

### Step 3: Test the Deployment

1. **Reload Web App:**
   - In Web tab, click "Reload ramez.pythonanywhere.com"
   - Wait for reload to complete

2. **Test API Endpoint:**
   - Open browser and go to: `https://ramez.pythonanywhere.com/api/items/`
   - Should return JSON data or Django REST framework page

3. **Check Error Logs:**
   - In Web tab, click "Error log"
   - Look for any Python/Django errors

## Alternative Solutions

### Option 1: Use Different PythonAnywhere URL

If `ramez.pythonanywhere.com` doesn't work, PythonAnywhere might have assigned a different URL:

1. Check your Web tab for the actual URL
2. Common formats:
   - `ramez.pythonanywhere.com`
   - `ramez.eu.pythonanywhere.com` (EU servers)
   - `webapp-XXXXX.pythonanywhere.com` (temporary URLs)

3. Update Flutter app with correct URL:
   ```dart
   static const String _baseUrl = 'https://YOUR_ACTUAL_URL/api';
   ```

### Option 2: Verify Account Type

1. **Free Account Limitations:**
   - Free accounts get `username.pythonanywhere.com`
   - Paid accounts can use custom domains

2. **Check Your Account:**
   - Go to "Account" tab
   - Verify your account type and limitations

## Testing Commands

Run these in PythonAnywhere Bash console:

```bash
# Navigate to project
cd /home/ramez/shopping_server
source venv/bin/activate

# Test Django
python manage.py check

# Test database
python manage.py migrate

# Test static files
python manage.py collectstatic --noinput

# Test server locally
python manage.py runserver
```

## Quick Fix for Development

While fixing PythonAnywhere, you can:

1. **Use Local Development Server:**
   ```bash
   cd shopping_server
   python manage.py runserver 0.0.0.0:8000
   ```

2. **Flutter app is already configured for localhost**
   - Current URL: `http://192.168.8.120:8000/api`
   - This will work with local Django server

## Final Steps

1. **Fix PythonAnywhere deployment** using steps above
2. **Test the live URL** in browser
3. **Update Flutter app** with working PythonAnywhere URL
4. **Test Flutter app** with live API

## Common PythonAnywhere Issues

- **WSGI file errors**: Check Python path and settings module
- **Static files not loading**: Verify static files configuration
- **Database errors**: Run migrations in console
- **Import errors**: Check virtual environment and requirements.txt

If issues persist, check PythonAnywhere error logs and forums for specific error messages.