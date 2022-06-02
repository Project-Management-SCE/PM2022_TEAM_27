from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase,Client,LiveServerTestCase
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

class workerstest(unittest.TestCase):

   def worker_exist(self):
        db_connection = mysql.connector.connect(
        host="database-1.c4joaqwcqrpg.eu-central-1.rds.amazonaws.com",
        user="admin",
        password="okoklol123",
        database="db_besce")
        cursor = db_connection.cursor()
        cursor.execute("SELECT fname FROM worker")
        result = cursor.fetchall()
        wfnames =  ["Snir",
                "Anthony",
                ]   
        for i in range(len(wfnames)):
            self.assertEqual(wfnames[i],result[i][0])
        cursor.close()

class adminstest(unittest.TestCase):

    def admin_exist(self):
        db_connection = mysql.connector.connect(
        host="database-1.c4joaqwcqrpg.eu-central-1.rds.amazonaws.com",
        user="admin",
        password="okoklol123",
        database="db_besce")
        cursor = db_connection.cursor()
        cursor.execute("SELECT fname FROM admin")
        result = cursor.fetchall()
        afnames =  ["Liron",
                "Kevyn",
                "Udi",
                ]   
        for i in range(len(afnames)):
            self.assertEqual(afnames[i],result[i][0])
        cursor.close()

    def test_adminslug(self):
       item=Admin()
       item.id=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()
       self.assertNotEqual(item.fname, 'udti')

class registertest(unittest.TestCase):
   '''
    def test_register(self):
       item=Client()
       item.id=11
       item.email='judith@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.fname = 'judith'
       item.lname = 'mars'
       item.bday = '20/07/1995'
       item.gender = 'Male'
       item.address = '29 okok'
       item.city = 'beer sheva'
       item.country = 'israel'
       item.phone = '0584545454'
       item.save()
       record= Client.objects.get()
       print("NewClient")
       self.assertEqual(record,item) 
   '''

   def test_registerslug(self):
       item=Client()
       item.id=11
       item.email='judith@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.save()
       self.assertNotEquals(item.email, '123456')


class productsstest(unittest.TestCase):

    def products_exist(self):
        db_connection = mysql.connector.connect(
        host="database-1.c4joaqwcqrpg.eu-central-1.rds.amazonaws.com",
        user="admin",
        password="okoklol123",
        database="db_besce")
        cursor = db_connection.cursor()
        cursor.execute("SELECT name FROM product")
        result = cursor.fetchall()
        names =  ["Acamol",
                "Loratadine Tablets",
                "Ritalin",
                ]   
        for i in range(len(names)):
            self.assertEqual(names[i],result[i][0])
        cursor.close()

class orderedsstest(unittest.TestCase):
   def status_exist(self):
        db_connection = mysql.connector.connect(
        host="database-1.c4joaqwcqrpg.eu-central-1.rds.amazonaws.com",
        user="admin",
        password="okoklol123",
        database="db_besce")
        cursor = db_connection.cursor()
        cursor.execute("SELECT status FROM ordered")
        result = cursor.fetchall()
        status =  ["Waiting",
                "Completed",
                ]   
        for i in range(len(status)):
            self.assertEqual(status[i],result[i][0])
        cursor.close()

class prescriptionsstest(unittest.TestCase):
   def status_exist(self):
        db_connection = mysql.connector.connect(
        host="database-1.c4joaqwcqrpg.eu-central-1.rds.amazonaws.com",
        user="admin",
        password="okoklol123",
        database="db_besce")
        cursor = db_connection.cursor()
        cursor.execute("SELECT pid FROM prescription")
        result = cursor.fetchall()
        pid =  [3
                ]   
        for i in range(len(pid)):
            self.assertEqual(pid[i],result[i][0])
        cursor.close()
'''
class PrescriptionTest(TestCase):

   def test_prescription(self):
        item=Prescription()
        item.id=11
        item.cid=5
        item.informations="okok"
        item.save()
        record=Prescription.objects.get()
        self.assertEqual(record,item)
        '''