# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labrab2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('cont_id', models.IntegerField(serialize=False, primary_key=True)),
                ('place', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]
