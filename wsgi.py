"""WSGI config for the MTG Helper project."""

import os

from django.core.wsgi import get_wsgi_application


if 'DJANGO_SETTING_MODULE' not in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
