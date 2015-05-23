# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labrab2', '0009_auto_20150524_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='contestant_place',
            field=models.IntegerField(),
        ),
    ]
