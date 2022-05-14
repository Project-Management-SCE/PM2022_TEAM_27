from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from BeSce.views import *
from BeSce.models import *
import unittest
from django.test.client import RequestFactory

# Create your tests here.

class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        url=reverse('index')
        url1=reverse('login')
        url2=reverse('adminlist')
        url3=reverse('workerlist')
        url4=reverse('clientlist')
        #url5=reverse('productlist')
        #url6=reverse('orderlist')
        #url7=reverse('nav_shop')
        #url8=reverse('nav_profil')
        #url9=reverse('myorder')
        print(resolve(url))
        print(resolve(url1))
        print(resolve(url2))
        print(resolve(url3))
        print(resolve(url4))
       #print(resolve(url5))
       #print(resolve(url6))
       #print(resolve(url7))
       #print(resolve(url8))
       #print(resolve(url9))

class workerstest(TestCase):

    def test_workers(self):
       item=Worker()
       item.id=10
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
       item.id=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()
       self.assertNotEqual(item.fname, 'udit')

class adminstest(TestCase):

    def test_admins(self):
       item=Admin()
       item.id=10
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
       item.id=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()
       self.assertNotEqual(item.fname, 'udti')

class registertest(TestCase):

    def test_register(self):
       item=Client()
       item.id=11
       item.email='judith@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.save()
       record= Client.objects.get()
       print("NewClient")
       self.assertEqual(record,item)

    def test_registerslug(self):
       item=Client()
       item.id=11
       item.email='judith@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.save()
       self.assertNotEquals(item.email, '123456')


