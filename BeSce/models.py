# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Client(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    idnumber = models.CharField(db_column='idnumber', max_length=9)
    fname = models.TextField(db_column='fname')
    lname = models.TextField(db_column='lname')
    bday = models.DateField(db_column='bday')
    type = models.TextField(db_column='type')
    address = models.TextField(db_column='address')
    city = models.TextField(db_column='city')
    country = models.TextField(db_column='country')
    phone = models.CharField(db_column='phone', max_length=11)

    class Meta:
        managed = False
        db_table = 'client'


class Director(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    idnumber = models.CharField(db_column='idnumber', max_length=9)
    fname = models.TextField(db_column='fname')
    lname = models.TextField(db_column='lname')

    class Meta:
        managed = False
        db_table = 'director'


class Pharmacian(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    idnumber = models.CharField(db_column='idnumber', max_length=9)
    fname = models.TextField(db_column='fname')
    lname = models.TextField(db_column='lname')

    class Meta:
        managed = False
        db_table = 'pharmacian'


class User(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    idnumber = models.CharField(db_column='idnumber', max_length=9)
    password = models.TextField(db_column='password', max_length=24)
    email = models.TextField(db_column='email')
    rank = models.TextField(db_column='rank')

    class Meta:
        managed = False
        db_table = 'user'
