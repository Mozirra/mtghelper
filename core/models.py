"""Core models used through the MTG Helper project."""

from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):

    """The different players for MTG."""

    class Meta:
        db_table = 'player'
        ordering = ['last_name', 'first_name']

    player_id = models.AutoField(primary_key=True)
    birthdate = models.DateField(null=True, blank=True)
    short_name = models.CharField(max_length=32)
