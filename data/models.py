"""Models used for storing statistics from games."""

import datetime

from django.conf import settings
from django.db import models


__all__ = ['Location', 'Outcome', 'GameType', 'Game', 'GameDeck']


class Location(models.Model):

    """Different locations where MTG games are played."""

    class Meta:
        db_table = 'location'
        ordering = ['name']

    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=256)


class Outcome(models.Model):

    """The different possible outcomes of a game."""

    class Meta:
        db_table = 'outcome'
        ordering = ['outcome']

    outcome_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8)


class GameType(models.Model):

    """The different variants of MTG games."""

    class Meta:
        db_table = 'game_type'
        ordering = ['name']

    game_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)


class TeamType(models.Model):

    """The different types of teams in a game."""

    class Meta:
        db_table = 'team_type'
        ordering = ['game_type__name', 'name']

    team_type_id = models.AutoField(primary_key=True)
    game_type = models.ForeignKey(GameType, models.CASCADE)
    name = models.CharField(max_length=64)


class Game(models.Model):

    """Information on the played games of MTG."""

    class Meta:
        db_table = 'game'
        ordering = ['date', 'game']

    game_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    length = models.TimeField()
    number_of_rounds = models.IntegerField()
    game_type = models.ForeignKey(GameType, models.CASCADE)
    location = models.ForeignKey(Location, models.CASCADE)


class GameDeck(models.Model):

    """Information on the different decks used in a game."""

    class Meta:
        db_table = 'game_deck'
        ordering = ['game__date', 'game', 'game_deck']

    game_deck_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, models.CASCADE)
    deck = models.ForeignKey('deck.Deck', models.CASCADE)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    round_eliminated = models.IntegerField()
    outcome = models.ForeignKey(Outcome, models.CASCADE)
    team_type = models.ForeignKey(TeamType, models.CASCADE)
