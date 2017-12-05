"""Stub file for core.models.py."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id: models.AutoField
    birthdate: models.DateField
    short_name: models.CharField
