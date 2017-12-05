"""Stub file for deck.models.py."""

from django.db import models


class Archetype(models.Model):
    archetype_id: models.AutoField
    name: models.CharField


class Color(models.Model):
    color_id: models.AutoField
    name: models.CharField
    white: models.BooleanField
    blue: models.BooleanField
    black: models.BooleanField
    red: models.BooleanField
    green: models.BooleanField


class Commander(models.Model):
    commander_id: models.AutoField
    name: models.CharField
    color_id: models.ForeignKey


class Deck(models.Model):
    deck_id: models.AutoField
    name: models.CharField
    user_id: models.ForeignKey
    commander_id: models.ForeignKey
    archetype_id: models.ForeignKey
    is_active: models.BooleanField
