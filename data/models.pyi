"""Stub file for data.models.py."""

from django.db import models


class Location(models.Model):
    location_id: models.AutoField
    name: models.CharField
    address: models.CharField


class Outcome(models.Model):
    outcome_id: models.AutoField
    name: models.CharField


class GameType(models.Model):
    game_type_id: models.AutoField
    name: models.CharField


class TeamType(models.Model):
    team_type_id: models.AutoField
    game_type_id: models.ForeignKey
    name: models.CharField


class Game(models.Model):
    game_id: models.AutoField
    date: models.DateField
    length: models.TimeField
    number_of_rounds: models.IntegerField
    game_type_id: models.ForeignKey
    location_id: models.ForeignKey


class GameDeck(models.Model):
    game_deck_id: models.AutoField
    game_id: models.ForeignKey
    deck_id: models.ForeignKey
    user_id: models.ForeignKey
    round_eliminated: models.IntegerField
    outcome_id: models.ForeignKey
    team_type_id: models.ForeignKey
