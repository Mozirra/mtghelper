#!/usr/bin/env python
"""Management tools for the Django application."""

import os
import sys

if 'DJANGO_SETTING_MODULE' not in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.core.management import execute_from_command_line


execute_from_command_line(sys.argv)
