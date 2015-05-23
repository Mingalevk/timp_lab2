# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labrab2', '0004_auto_20150523_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='cont_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
        ),
    ]
