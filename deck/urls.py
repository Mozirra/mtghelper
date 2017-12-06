"""The "Deck" application URL configuration."""

from django.urls import path
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from deck.models import Commander, Deck


__all__ = ['urlpatterns']


urlpatterns = [
    # Commander URLs
    path('commander/list', ListView.as_view(model=Commander)),
    path(
        'commander/new',
        CreateView.as_view(model=Commander, fields=['name', 'color'])
    ),
    # Deck URLs
    path('list', ListView.as_view(model=Deck)),
    path(
        'new',
        CreateView.as_view(
            model=Deck,
            fields=['name', 'player', 'commander', 'archetype']
        )
    ),
    path('details/<int:pk>', DetailView.as_view(model=Deck)),
    path(
        'update/<int:pk>',
        UpdateView.as_view(
            model=Deck,
            fields=['name', 'player', 'commander', 'archetype']
        )
    )
]
