"""
WSGI config for ost_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ost_project.settings")

sys.path.append('/home/ubuntu/ost_project/')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
