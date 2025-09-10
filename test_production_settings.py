#!/usr/bin/env python
"""
Test script to verify production settings work correctly
Run this on PythonAnywhere to test the configuration
"""

import os
import sys

# Add project paths
project_path = '/home/ramez/shopping_server/shopping_server'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

parent_path = '/home/ramez/shopping_server'
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

root_path = '/home/ramez'
if root_path not in sys.path:
    sys.path.insert(0, root_path)

def test_production_settings():
    """Test production settings configuration"""
    try:
        # Set production settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_server.settings_production')
        
        # Import Django and setup
        import django
        django.setup()
        
        # Test settings
        from django.conf import settings
        
        print("✅ Production settings loaded successfully!")
        print(f"DEBUG: {settings.DEBUG}")
        print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        print(f"INSTALLED_APPS count: {len(settings.INSTALLED_APPS)}")
        
        # Check for duplicates in INSTALLED_APPS
        apps = settings.INSTALLED_APPS
        duplicates = [app for app in set(apps) if apps.count(app) > 1]
        if duplicates:
            print(f"❌ Duplicate apps found: {duplicates}")
        else:
            print("✅ No duplicate apps found")
            
        # Test WSGI application
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        print("✅ WSGI application created successfully!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_api_imports():
    """Test API-related imports"""
    try:
        from shopping_list.models import Item
        from shopping_list.serializers import ItemSerializer
        from shopping_list.views import ItemViewSet
        print("✅ API imports successful!")
        return True
    except Exception as e:
        print(f"❌ API import error: {e}")
        return False

if __name__ == '__main__':
    print("Testing PythonAnywhere Production Configuration...")
    print("=" * 50)
    
    settings_ok = test_production_settings()
    api_ok = test_api_imports()
    
    print("=" * 50)
    if settings_ok and api_ok:
        print("🎉 All tests passed! Your configuration is ready for deployment.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")