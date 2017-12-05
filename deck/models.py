"""Models related to storing deck information."""

from django.conf import settings
from django.db import models


__all__ = ['Archetype', 'Color', 'Commander', 'Deck']


class Archetype(models.Model):

    """The different deck archetypes."""

    class Meta:
        db_table = 'archetype'

    archetype_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)


class Color(models.Model):

    """The different color combinations possible in MTG."""

    class Meta:
        db_table = 'color'
        ordering = ['color']
        unique_together = ('white', 'blue', 'black', 'red', 'green')

    color_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True)
    white = models.BooleanField()
    blue = models.BooleanField()
    black = models.BooleanField()
    red = models.BooleanField()
    green = models.BooleanField()


class Commander(models.Model):

    """The different commanders for decks."""

    class Meta:
        db_table = 'commander'
        ordering = ['name']

    commander_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    color = models.ForeignKey(Color, models.CASCADE)


class Deck(models.Model):

    """The different decks of the users."""

    class Meta:
        db_table = 'deck'
        ordering = ['user__last_name', 'user__first_name', 'commander__name']

    deck_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    commander = models.ForeignKey(Commander, models.CASCADE)
    archetype = models.ForeignKey(Archetype, models.CASCADE)
    is_active = models.BooleanField(default=True)
