# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foosball', '0003_scorechange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorechange',
            name='change',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scorechange',
            name='game',
            field=models.ForeignKey(related_name='score_changes', to='foosball.Game'),
        ),
        migrations.AlterField(
            model_name='scorechange',
            name='player',
            field=models.ForeignKey(related_name='score_changes', to='foosball.Player'),
        ),
    ]
