"""Stub file for core.models.py."""

import datetime
import typing

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    user_id: int
    birthdate: datetime.date
    short_name: str
