from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
from .decorators import *
from BeSce.models import User
from BeSce.models import Client
from BeSce.models import Pharmacian
from BeSce.models import Director
# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="besce_db")

cursor = db_connection.cursor()
print(db_connection)


#Index Page - return the first main page
def index(request):
    return render(request,'index.html')

#Login page - return the login/register page
def login(request):
    return render(request,'login.html')

def client_registration(request):
    return render(request,'Registration/client_registration.html')

def FirstTimePage(request):
    return render(request,'FirstTimePage.html')

def cindex(request):
    return render(request, 'client_templates/index.html')

# --- Functions --- #

def f_register(request):
    if request.method=='POST':
        save_record=User()
        checker=request.POST.get('idnumber')
        save_record.idnumber=request.POST.get('idnumber')
        save_record.password=request.POST.get('pass')
        save_record.email=request.POST.get('email')
        save_record.rank="0"
        if check_user_idnumber(checker)== False:
            messages.error(request,'This Id Number is already exist!') 
            return login(request)
        save_record.save()
        messages.success(request, 'Thank you for your registration!')
        return login(request)
    else:
        return login(request)

#@unautheticated_user
def f_login(request):
    result = []
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    if request.method=='POST':
        v_idnumber=request.POST.get('idnumber')
        v_password=request.POST.get('pass')
        for item in data:
            id,idnumber,password,email,rank= item
            if v_idnumber==idnumber and v_password == password and rank == "0":
                return FirstTimePage(request)
            elif v_idnumber==idnumber and v_password == password and rank == "1":
                return cindex(request)
            elif v_idnumber==idnumber and v_password == password and rank == "2":
                return WorkerDashboard(request)
            elif v_idnumber==idnumber and v_password == password and rank == "3":
                return AdminDashboard(request) 
        else :
            messages.error(request,'Not correct, please try again!')   
            return index(request)

def f_cregister(request):
    if request.method=='POST':
        result = []
        save_record_rank=User()
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        for item in data:
            id,idnumber,password,email,rank= item
            if request.POST.get('idnumber')==idnumber and save_record_rank.rank=="0":
                save_record_rank.rank="1"
                save_record_client=Client()
                cursor.execute("SELECT * FROM client")
                data = cursor.fetchall()
                for item in data:
                    id,idnumber, fname, lname, bday, type, address, city, country, phone = item
                    save_record_client.idnumber=request.POST.get('idnumber')
                    save_record_client.fname=request.POST.get('fname')
                    save_record_client.lname=request.POST.get('lname')
                    save_record_client.bday=request.POST.get('bday')
                    save_record_client.type=request.POST.get('gender')
                    save_record_client.address=request.POST.get('address')
                    save_record_client.city=request.POST.get('city')
                    save_record_client.country=request.POST.get('country')
                    save_record_client.phone=request.POST.get('phone')
                    save_record_client.save()
                    messages.success(request, 'Thank you for your registration!')
                    return cindex(request)
    else:
        return login(request)

def check_user_idnumber(idnum):
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    for item in data:
        id,idnumber,password,email,rank= item
        if idnum==idnumber:
            return False
