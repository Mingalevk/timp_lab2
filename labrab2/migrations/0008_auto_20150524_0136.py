# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labrab2', '0007_auto_20150524_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='contestant_place',
            field=models.IntegerField(default=b'none'),
        ),
    ]
