"""Models related to storing deck information."""

from django.conf import settings
from django.db import models


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

    color_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    white = models.BooleanField()
    blue = models.BooleanField()
    black = models.BooleanField()
    red = models.BooleanField()
    green = models.BooleanField()


class Commander(models.Model):

    """The different commanders for decks."""

    class Meta:
        db_table = 'commander'

    commander_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    color_id = models.ForeignKey(Color, models.CASCADE)


class Deck(models.Model):

    """The different decks of the users."""

    class Meta:
        db_table = 'deck'

    deck_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    commander_id = models.ForeignKey(Commander, models.CASCADE)
    archetype_id = models.ForeignKey(Archetype, models.CASCADE)
    is_active = models.BooleanField(default=True)
