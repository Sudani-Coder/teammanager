from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    details = models.TextField()

    def __str__(self):
        return self.name

class Player(models.Model):
    the_position = (
        ('1', 'حارس'),
        ('2', 'دفاع'),
        ('3', 'وسط'),
        ('4', 'هجوم')
    )
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    age = models.IntegerField()
    position_in_field = models.CharField(max_length=200, choices=the_position)
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} - {self.team}"

class GameScore(models.Model):
    first_team = models.CharField(max_length=200)
    second_team = models.CharField(max_length=200)
    first_team_score = models.IntegerField(default=0)
    second_team_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_team} {self.first_team_score} - {self.second_team} {self.second_team_score}"
