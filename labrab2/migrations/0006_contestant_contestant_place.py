# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labrab2', '0005_auto_20150523_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='contestant_place',
            field=models.IntegerField(null=True),
        ),
    ]
