# Generated by Django 3.1.2 on 2020-10-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team', models.CharField(max_length=200)),
                ('second_team', models.CharField(max_length=200)),
                ('first_team_score', models.IntegerField(default=0)),
                ('second_team_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('position_in_field', models.CharField(choices=[('1', 'حارس'), ('2', 'دفاع'), ('3', 'وسط'), ('4', 'هجوم')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('details', models.TextField()),
            ],
        ),
    ]
