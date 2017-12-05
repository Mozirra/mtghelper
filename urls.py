"""The MTG Helper URL configuration."""

from django.urls import include, path


__all__ = ['urlpatterns']


urlpatterns = [
    path('deck/', include('deck.urls')),
    path('data/', include('data.urls')),
]
