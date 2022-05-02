from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from BeSce.views import *
from BeSce.models import *
import unittest
from django.test.client import RequestFactory

# Create your tests here.

class workerstest(TestCase):

    def test_workers(self):
       item=Worker()
       item.ID=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()
       record= Worker.objects.get()
       print("WORKERSS")
       self.assertEqual(record,item)

    def test_workerslug(self):
       item=Worker()
       item.ID=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()

       self.assertEqual(item.fname, 'udit')

class adminstest(TestCase):

    def test_admins(self):
       item=Admin()
       item.ID=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()
       record= Admin.objects.get()
       print("ADMINSS")
       self.assertEqual(record,item)

    def test_adminslug(self):
       item=Admin()
       item.ID=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()

       self.assertEqual(item.fname, 'udit')

class registertest(TestCase):

    def test_register(self):
       item=Client()
       item.ID=11
       item.email='judith@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.save()
       record= Client.objects.get()
       print("NewClient")
       self.assertEqual(record,item)

    def test_registerslug(self):
       item=Client()
       item.ID=11
       item.email='judith@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.save()
       self.assertNotEquals(item.email, '123456')


