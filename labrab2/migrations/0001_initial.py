# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sportsmen',
            fields=[
                ('sportsman_id', models.IntegerField(default=0, unique=True, serialize=False, primary_key=True)),
                ('sportsman_fio', models.CharField(max_length=30)),
                ('sportsman_country', models.CharField(max_length=20)),
                ('sportsman_bdate', models.DateField(verbose_name=b'date_published')),
            ],
        ),
        migrations.AddField(
            model_name='contestant',
            name='contestant',
            field=models.ForeignKey(to='labrab2.Sportsmen'),
        ),
    ]
