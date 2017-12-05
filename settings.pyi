"""Stub file for settings.py."""

import typing


BASE_DIR: str
SECRET_KEY: str
DEBUG: bool
ALLOWED_HOSTS: typing.List[str]
INSTALLED_APPS: typing.List[str]
MIDDLEWARE: typing.List[str]
ROOT_URLCONF: str
TEMPLATES: typing.List[typing.Dict[str, typing.Any]]
WSGI_APPLICATION: str
DATABASES: typing.Dict[str, typing.Dict[str, str]]
AUTH_PASSWORD_VALIDATORS: typing.List[typing.Dict[str, str]]
LANGUAGE_CODE: str
TIME_ZONE: str
USE_I18N: bool
USE_L10N: bool
USE_TZ: bool
STATIC_URL: str
