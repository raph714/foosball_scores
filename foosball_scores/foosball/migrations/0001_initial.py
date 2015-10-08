# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('team_a_score', models.PositiveIntegerField(default=0)),
                ('team_b_score', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('score', models.PositiveIntegerField(default=1000)),
                ('wins', models.PositiveIntegerField(default=0)),
                ('losses', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='team_a_players',
            field=models.ManyToManyField(related_name='team_a_games', to='foosball.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_b_players',
            field=models.ManyToManyField(related_name='team_b_games', to='foosball.Player'),
        ),
    ]
