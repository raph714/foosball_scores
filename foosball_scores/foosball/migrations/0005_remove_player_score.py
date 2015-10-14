# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foosball', '0004_auto_20151014_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='score',
        ),
    ]
