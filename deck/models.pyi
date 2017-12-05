"""Stub file for deck.models.py."""

import typing

from django.db import models

from core.models import User


class Archetype(models.Model):

    class Meta:
        db_table: str

    archetype_id: int
    name: str


class Color(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]
        unique_together: typing.Tuple[str, str, str, str, str]

    color_id: int
    name: str
    white: bool
    blue: bool
    black: bool
    red: bool
    green: bool


class Commander(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]

    commander_id: int
    name: str
    color: Color


class Deck(models.Model):

    class Meta:
        db_table: str
        ordering: typing.List[str]
        
    deck_id: int
    name: str
    user: User
    commander: Commander
    archetype: Archetype
    is_active: bool
