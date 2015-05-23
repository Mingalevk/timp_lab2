# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labrab2', '0006_contestant_contestant_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='cont_id',
            new_name='id',
        ),
        migrations.AddField(
            model_name='contestant',
            name='contest',
            field=models.ForeignKey(default=1, to='labrab2.Contest'),
            preserve_default=False,
        ),
    ]
