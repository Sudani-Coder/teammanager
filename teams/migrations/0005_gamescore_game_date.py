# Generated by Django 3.1.2 on 2020-10-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20201020_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='game_date',
            field=models.DateField(auto_now=True),
        ),
    ]
