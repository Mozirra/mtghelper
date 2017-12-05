"""Stub file for data.models.py."""

import datetime
import typing

from django.db import models

from core.models import User
from deck.models import Deck


class Location(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    location_id: int
    name: str
    address: str


class Outcome(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    outcome_id: int
    name: str


class GameType(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    game_type_id: int
    name: str


class TeamType(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    team_type_id: int
    game_type: GameType
    name: str


class Game(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    game_id: int
    date: datetime.date
    length: datetime.time
    number_of_rounds: int
    game_type: GameType
    location: Location


class GameDeck(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    game_deck_id: int
    game: Game
    deck: Deck
    user: User
    round_eliminated: int
    outcome: Outcome
    team_type: TeamType
