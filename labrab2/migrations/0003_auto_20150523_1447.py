# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labrab2', '0002_contest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportsmen',
            old_name='sportsman_bdate',
            new_name='bdate',
        ),
        migrations.RenameField(
            model_name='sportsmen',
            old_name='sportsman_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='sportsmen',
            old_name='sportsman_fio',
            new_name='fio',
        ),
        migrations.RenameField(
            model_name='sportsmen',
            old_name='sportsman_id',
            new_name='id',
        ),
    ]
