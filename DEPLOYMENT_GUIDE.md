# Django Shopping App - PythonAnywhere Deployment Guide

This guide will help you deploy your Django shopping app to PythonAnywhere (ramez.pythonanywhere.com).

## Prerequisites

- PythonAnywhere account (ramez.pythonanywhere.com)
- Your Django project files
- Basic knowledge of terminal/console commands

## Step 1: Upload Your Project

1. **Login to PythonAnywhere**
   - Go to https://www.pythonanywhere.com/
   - Login with your account (ramez)

2. **Open a Bash Console**
   - Go to "Tasks" → "Consoles"
   - Click "Bash"

3. **Upload your project files**
   ```bash
   # Create project directory
   mkdir shopping_server
   cd shopping_server
   
   # Upload your files using the Files tab or git clone
   # If using git:
   # git clone <your-repository-url> .
   ```

## Step 2: Install Dependencies

1. **Create a virtual environment**
   ```bash
   cd /home/ramez/shopping_server
   python3.10 -m venv venv
   source venv/bin/activate
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

## Step 3: Configure Database

1. **Run migrations**
   ```bash
   cd /home/ramez/shopping_server
   python manage.py migrate
   ```

2. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

3. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

## Step 4: Configure Web App

1. **Go to Web tab**
   - In PythonAnywhere dashboard, click "Web"
   - Click "Add a new web app"

2. **Choose Manual Configuration**
   - Select "Manual configuration"
   - Choose Python 3.10

3. **Configure WSGI file**
   - In the Web tab, find "Code" section
   - Click on the WSGI configuration file link
   - Replace the content with the content from `wsgi_pythonanywhere.py`

4. **Set up Virtual Environment**
   - In "Virtualenv" section, enter:
     ```
     /home/ramez/shopping_server/venv
     ```

5. **Configure Static Files**
   - In "Static files" section, add:
     - URL: `/static/`
     - Directory: `/home/ramez/shopping_server/static/`

## Step 5: Environment Configuration

1. **Update settings**
   - Make sure to use `settings_production.py` for production
   - Update the WSGI file to use production settings:
     ```python
     os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping_server.settings_production'
     ```

2. **Security Settings**
   - Generate a new SECRET_KEY for production
   - Update ALLOWED_HOSTS in settings_production.py
   - Set DEBUG = False

## Step 6: Test Your Deployment

1. **Reload your web app**
   - In the Web tab, click "Reload ramez.pythonanywhere.com"

2. **Test API endpoints**
   - Visit: `https://ramez.pythonanywhere.com/api/items/`
   - Should return JSON response

3. **Test admin panel**
   - Visit: `https://ramez.pythonanywhere.com/admin/`
   - Login with superuser credentials

## API Endpoints

Your API will be available at:
- `GET/POST https://ramez.pythonanywhere.com/api/items/` - List/Create items
- `GET/PUT/DELETE https://ramez.pythonanywhere.com/api/items/{id}/` - Item details
- `GET https://ramez.pythonanywhere.com/api/items/?search=query` - Search items

## Flutter App Configuration

Update your Flutter app's API base URL to:
```dart
static const String _baseUrl = 'https://ramez.pythonanywhere.com/api';
```

## Troubleshooting

### Common Issues:

1. **500 Internal Server Error**
   - Check error logs in PythonAnywhere Web tab
   - Verify WSGI configuration
   - Check virtual environment path

2. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check static files configuration in Web tab

3. **Database errors**
   - Run migrations: `python manage.py migrate`
   - Check database file permissions

4. **CORS errors from Flutter**
   - Verify CORS settings in `settings_production.py`
   - Add your Flutter app domain to CORS_ALLOWED_ORIGINS

### Useful Commands:

```bash
# Activate virtual environment
source /home/ramez/shopping_server/venv/bin/activate

# Check Django version
python -m django --version

# Run Django shell
python manage.py shell

# View logs
tail -f /var/log/ramez.pythonanywhere.com.error.log
```

## Security Notes

- Always use HTTPS in production
- Keep your SECRET_KEY secure and unique
- Regularly update dependencies
- Monitor your application logs
- Use strong passwords for admin accounts

## Support

For PythonAnywhere specific issues, check:
- PythonAnywhere Help pages
- PythonAnywhere Forums
- Django documentation

---

**Your Django Shopping API is now deployed at: https://ramez.pythonanywhere.com/**