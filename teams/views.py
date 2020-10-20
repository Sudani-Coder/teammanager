from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View
from django.views.generic import *
from teams.models import *

class index(View):
    def get(self, request):
        all_teams = Team.objects.all()
        template = "index.html"
        context = {"teams": all_teams}
        return render(request, template, context)

class TeamsListView(ListView):
    model = Team
    template_name = "team_list.html"
    context_object_name = "teams"

class ScoresListView(ListView):
    model = GameScore
    template_name = "score_list.html"
    context_object_name = "scores"

class TeamDetailView(DetailView):
    model = Team
    template_name = "team_detail.html"
    context_object_name = "team"
    slug_field = "name"

class PlayerDetailView(DetailView):
    model = Player
    template_name = "player_detail.html"
    context_object_name = "player"
    slug_field = "name"
