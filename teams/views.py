# from django.db import IntegrityError
# from django.http import HttpResponse

from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import *

from teams.forms import *
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

    def get_context_data(self, **kwargs) -> dict:
        context = super(ScoresListView, self).get_context_data(**kwargs)
        context['form'] = ScoreModelForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ScoreModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index/scores/')

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

class AddTeamView(View):
    def get(self, request):
        form = TeamModelForm()
        context = {'form': form}
        template = 'add_team.html'
        return render(request, template, context)
    
    def post(self, request):
        form = TeamModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            template = 'add_team.html'
            context = {'form': form}
            return render(request, template, context)
