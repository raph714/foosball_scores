# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foosball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='scores_calculated',
            field=models.BooleanField(default=False),
        ),
    ]
