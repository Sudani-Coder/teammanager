from django.urls import path

from teams.views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('teams/', TeamsListView.as_view(), name='teams'),
    path('scores/', ScoresListView.as_view(), name='scores'),
    path('player/<slug:slug>/', PlayerDetailView.as_view(), name='player'),
    path('team/<slug:slug>/', TeamDetailView.as_view(), name='team'),
]
