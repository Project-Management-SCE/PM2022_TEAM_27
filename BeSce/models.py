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

# ============== USERS MODELS ============== #

class Admin(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    idnumber = models.CharField(db_column='idnumber',max_length=11)
    password = models.TextField(db_column='password')
    fname = models.TextField(db_column='fname')
    lname = models.TextField(db_column='lname')

    class Meta:
        managed = False
        db_table = 'admin'


class Client(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    idnumber = models.CharField(db_column='idnumber',max_length=11)
    email = models.TextField(db_column='email')
    password = models.TextField(db_column='password')
    fname = models.TextField(db_column='fname',blank=True, null=True)
    lname = models.TextField(db_column='lname',blank=True, null=True)
    bday = models.DateField(db_column='bday',blank=True, null=True)
    gender = models.TextField(db_column='gender',blank=True, null=True)
    address = models.TextField(db_column='address',blank=True, null=True)
    city = models.TextField(db_column='city',blank=True, null=True)
    country = models.TextField(db_column='country',blank=True, null=True)
    phone = models.CharField(db_column='phone',max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Worker(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    idnumber = models.CharField(db_column='idnumber',max_length=11)
    password = models.TextField(db_column='password')
    fname = models.TextField(db_column='fname')
    lname = models.TextField(db_column='lname')

    class Meta:
        managed = False
        db_table = 'worker'

# ============== USERS MODELS ============== #

class Product(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    name = models.TextField(db_column='name',)
    supplier = models.TextField(db_column='supplier',)
    type = models.TextField(db_column='type',)
    price = models.DecimalField(db_column='price',max_digits=10, decimal_places=2)
    stock = models.IntegerField(db_column='stock')
    prescription = models.TextField(db_column='prescription')

    class Meta:
        managed = False
        db_table = 'product'


class Ordershop(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    cid = models.IntegerField(db_column='cid')
    pid = models.TextField(db_column='pid')
    quantity = models.IntegerField(db_column='quantity')

    class Meta:
        managed = False
        db_table = 'ordershop'


class Ordered(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    cid = models.IntegerField()
    pid = models.ForeignKey('Product', models.DO_NOTHING, db_column='pid')
    quantity = models.ForeignKey('self', models.DO_NOTHING, db_column='quantity')
    wid = models.IntegerField(db_column='wid', blank=True, null=True)
    total = models.DecimalField(db_column='total', max_digits=10, decimal_places=2)
    status = models.TextField(db_column='status')

    class Meta:
        managed = False
        db_table = 'ordered'


class Prescription(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    cid = models.ForeignKey(Client, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    pid = models.IntegerField(db_column='pid')
    informations = models.TextField(db_column='informations')

    class Meta:
        managed = False
        db_table = 'prescription'
        
class Appointment(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    name = models.TextField(db_column='name')
    mail = models.TextField(db_column='mail')
    date_b = models.DateField(db_column='date_b')
    date_t = models.DateField(db_column='date_t')
    phone = models.TextField(db_column='phone')
    messege = models.TextField(db_column='messege')
    health_type = models.TextField(db_column='health_type')
    class Meta:
        managed = False
        db_table = 'appointment'


