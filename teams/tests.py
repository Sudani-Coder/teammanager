from django.http import response
from django.test import TestCase
from django.views.generic import detail

from teams.models import Team
# Create your tests here.
class ModelsTestCase(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='فريقي', details='فريق الاختبار')
        self.assertEqual(team.name, 'فريقي')

class ViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name='فريقي', details='فريق الاختبار')
        self.team1 = Team.objects.create(name='الفريق الاول', details='هذا هو الفريق الاول في القائمة')
        self.team2 = Team.objects.create(name='الفريق الثاني', details='هذا هو الفريق الثاني في القائمة')

    def test_teams_list_view(self):
        response = self.client.get('/index/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.team1, response.context['teams'])
        self.assertIn(self.team2, response.context['teams'])
        self.assertTemplateUsed(response, 'team_list.html')
        self.assertContains(response, self.team1.name)

    def test_team_detail_view(self):
        response = self.client.get('/index/team/فريقي/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.team, response.context['team'])
