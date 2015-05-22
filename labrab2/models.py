from django.db import models
#from django.contrib import admin


class Sportsmen(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=0)
    fio = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    bdate = models.DateField('date_published')


class Contest(models.Model):
    cont_id = models.IntegerField(primary_key=True)
    place = models.CharField(max_length=30)
    type = models.CharField(max_length=30)


class Contestant(models.Model):
    contestant = models.ForeignKey(Sportsmen)
    contestant_place = models.IntegerField


