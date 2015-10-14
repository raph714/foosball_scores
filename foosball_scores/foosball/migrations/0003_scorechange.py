# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foosball', '0002_game_scores_calculated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change', models.PositiveIntegerField(default=0)),
                ('game', models.ForeignKey(to='foosball.Game')),
                ('player', models.ForeignKey(to='foosball.Player')),
            ],
        ),
    ]
