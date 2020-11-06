from django.forms import *

from teams.models import *

class TeamModelForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            'name': 'اسم الفريق',
            'details': 'تفاصيل الفريق',
        }
        widgets = {
            'details': Textarea(attrs={'cols': 25, 'rows': 5}),
        }
        error_messages = {
            'name': {
                'unique': 'هذا الفريق مكرر ، يرجى التأكد من اسم الفريق',
            }
        }

class ScoreModelForm(ModelForm):
    class Meta:
        model = GameScore
        exclude = ['game_date']
        labels = {
            'first_team': 'الفريق الاول',
            'second_team': 'الفريق الثاني',
            'first_team_score': 'نتيجة الفريق الاول',
            'second_team_score': 'نتيجة الفريق الثاني',
        }
