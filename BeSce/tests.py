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
        url2=reverse('clin')
        url3=reverse('clmyor')
        url4=reverse('clpay')
        url5=reverse('clpayok')
        url6=reverse('clpro')
        url7=reverse('wkin')
        url8=reverse('wkkkpr')
        url9=reverse('wkneor')
        url10=reverse('wkmyor')
        url11=reverse('adin')
        url12=reverse('adadlt')
        url13=reverse('adcllt')
        url14=reverse('adorlt')
        url15=reverse('adorzlt')
        url16=reverse('adprdlt')
        url17=reverse('adwklt')
        url18=reverse('adprlt')

        print(resolve(url))
        print(resolve(url1))
        print(resolve(url2))
        print(resolve(url3))
        print(resolve(url4))
        print(resolve(url5))
        print(resolve(url6))
        print(resolve(url7))
        print(resolve(url8))
        print(resolve(url9))
        print(resolve(url10))
        print(resolve(url11))
        print(resolve(url12))
        print(resolve(url13))
        print(resolve(url14))
        print(resolve(url15))
        print(resolve(url16))
        print(resolve(url17))
        print(resolve(url18))

class workerstest(unittest.TestCase):

   def worker_exist_Integration(self):
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

class workertest(TestCase):
    def worker1(self):   
       item=Worker()
       item.id=10
       item.fname='almog'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Ohayon'
       item.save()
       record= Worker.objects.get()
       self.assertEqual(record,item) 

    def worker2(self):   
       item=Worker()
       item.id=11
       item.fname='Dina'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Ohayon'
       item.save()
       record= Worker.objects.get()
       self.assertEqual(record,item) 

    def worker3(self):   
       item=Worker()
       item.id=12
       item.fname='Frank'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Ohayon'
       item.save()
       record= Worker.objects.get()
       self.assertEqual(record,item) 

    def test_workerslug(self):
       item=Worker()
       item.id=10
       item.fname='Mike'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Boutboul'
       item.save()
       self.assertNotEqual(item.password, '123yadaimalarosh')

class adminstest(unittest.TestCase):

    def admin_exist_Integration(self):
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

    def admintest1(self):   
       item=Admin()
       item.id=12
       item.fname='Frank'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Ohayon'
       item.save()
       record= Admin.objects.get()
       self.assertEqual(record,item) 

    def admintest2(self):   
       item=Admin()
       item.id=13
       item.fname='Dona'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Web'
       item.save()
       record= Admin.objects.get()
       self.assertEqual(record,item)

    def admintest3(self):   
       item=Admin()
       item.id=14
       item.fname='Sylvie'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Walala'
       item.save()
       record= Admin.objects.get()
       self.assertEqual(record,item)

    def test_adminslug(self):
       item=Admin()
       item.id=10
       item.fname='udi'
       item.idnumber='123456789'
       item.password='123456'
       item.lname='Konrad'
       item.save()
       self.assertNotEqual(item.lname, 'Norman')

class registertest(TestCase):
   
    def test_register1(self):
       item=Client()
       item.id=11
       item.email='judith@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.fname = 'judith'
       item.lname = 'mars'
       item.bday = '1994-07-20'
       item.gender = 'Female'
       item.address = '29 okok'
       item.city = 'beer sheva'
       item.country = 'israel'
       item.phone = '0584545454'
       item.save()
       record= Client.objects.get()
       print("NewClient")
       self.assertEqual(record,item) 

    def test_register2(self):
       item=Client()
       item.id=11
       item.email='edi@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.fname = 'Eddie'
       item.lname = 'Pump'
       item.bday = '1995-07-20'
       item.gender = 'Male'
       item.address = '59 okok'
       item.city = 'Beer sheva'
       item.country = 'israel'
       item.phone = '0584545444'
       item.save()
       record= Client.objects.get()
       print("NewClient")
       self.assertEqual(record,item) 

    def test_register3(self):
       item=Client()
       item.id=11
       item.email='doc@gmail.com'
       item.idnumber='123456789'
       item.password='123456'
       item.fname = 'doctor'
       item.lname = 'pepper'
       item.bday = '1996-07-20'
       item.gender = 'Male'
       item.address = '2 kok'
       item.city = 'beer sheva'
       item.country = 'israel'
       item.phone = '0584333454'
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


class productsstest(unittest.TestCase):

    def products_exist_Integration(self):
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
'''
class ProductTest(TestCase):
    def test_product(self):
       item=Product()
       item.id=2
       item.name='Acamomol'
       item.supplier='50mgbycapsule'
       item.type='General'
       item.price =8
       item.stock =9
       item.prescription ='No'
       item.save()
       record= Product.objects.get()
       print("NewProduct")
       self.assertEqual(record,item) 
'''
class orderedsstest(unittest.TestCase):
    def status_exist_Integration(self):
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

class ordershoptest(TestCase):
    def ordershopTest1(self):
        item=Ordershop()
        item.id=11
        item.cid=5
        item.pid=3
        item.quantity=4
        item.save()
        record=Ordershop.objects.get()
        self.assertEqual(record,item)

    def ordershopTest2(self):
        item=Ordershop()
        item.id=12
        item.cid=5
        item.pid=4
        item.quantity=1
        item.save()
        record=Ordershop.objects.get()
        self.assertEqual(record,item)

    def ordershopTest3(self):
        item=Ordershop()
        item.id=13
        item.cid=5
        item.pid=1
        item.quantity=4
        item.save()
        record=Ordershop.objects.get()
        self.assertEqual(record,item)

class prescriptionsTest_Integration(unittest.TestCase):
    def status_exist_Integration(self):
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

class PrescriptionTest(TestCase):

    def test_prescription1(self):
        item=Prescription()
        item.id=11
        item.cid=5
        item.pid=23
        item.informations="okok"
        item.save()
        record=Prescription.objects.get()
        self.assertEqual(record,item)

    def test_prescription2(self):
        item=Prescription()
        item.id=12
        item.cid=5
        item.pid=232
        item.informations="Good"
        item.save()
        record=Prescription.objects.get()
        self.assertEqual(record,item)

    def test_prescription3(self):
        item=Prescription()
        item.id=13
        item.cid=5
        item.pid=3
        item.informations="ForDrugs"
        item.save()
        record=Prescription.objects.get()
        self.assertEqual(record,item)

    def test_prescription4(self):
        item=Prescription()
        item.id=14
        item.cid=5
        item.pid=2
        item.informations="Itsokforim"
        item.save()
        record=Prescription.objects.get()
        self.assertEqual(record,item)

    def test_prescriptionslug(self):
        item=Prescription()
        item.id=14
        item.cid=5
        item.pid=2
        item.informations="Itsokforim"
        item.save()
        self.assertNotEquals(item.informations, '123456')
