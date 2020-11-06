from django.urls import path, re_path

from teams.views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('teams/', TeamsListView.as_view(), name='teams'),
    path('scores/', ScoresListView.as_view(), name='scores'),
    re_path('^player/(?P<slug>[\w\x20]+)/$', PlayerDetailView.as_view(), name='player'),
    re_path('^team/(?P<slug>[-\w\x20]+)/$', TeamDetailView.as_view(), name='team'),
    path('add_team/', AddTeamView.as_view(), name='add_team')
]
