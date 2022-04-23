from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
from BeSce.models import Client
from BeSce.models import Worker
from BeSce.models import Admin
# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="db_besce")

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

def ClientDashboard(request):
    return render(request, 'client_templates/clientdashboard.html')

def ClientIndex(request):
    return render(request, 'client_templates/index.html')

def WorkerDashboard(request):
    return render(request, 'worker_templates/index.html')

def AdminDashboard(request):
    return render(request, 'admin_templates/index.html')

def ClientProfil(request):
    return render(request, 'client_templates/profil.html')


# --- Basics Functions --- #

def f_register(request):
    if request.method=='POST':
        save_record=Client()
        checker=request.POST.get('idnumber')
        save_record.idnumber=request.POST.get('idnumber')
        save_record.password=request.POST.get('pass')
        save_record.email=request.POST.get('email')
        if check_client_idnumber(checker)== True:
            messages.error(request,'This Id Number is already exist!') 
            return login(request)
        save_record.save()
        messages.success(request, 'Thank you for your registration!')
        return login(request)
    else:
        return login(request)

#@unautheticated_user
def f_login(request):
    if request.method=='POST':
        v_idnumber=request.POST.get('idnumber')
        v_password=request.POST.get('pass')
        admincheck=Admin.objects.filter(idnumber=v_idnumber,password=v_password)
        workercheck=Worker.objects.filter(idnumber=v_idnumber,password=v_password)
        clientcheck=Client.objects.filter(idnumber=v_idnumber,password=v_password)
        if admincheck:
            return render(request ,'admin_templates/index.html', {"admin1":admincheck})
        elif workercheck:
            return render(request ,'worker_templates/index.html', {"worker1":workercheck})
        elif clientcheck:

            return render(request ,'client_templates/profil.html', {"client1":clientcheck})
    else :
        messages.error(request,'Not correct, please try again!')   
        return login(request)

def check_client_idnumber(idnum):
    cursor.execute("SELECT * FROM client")
    data = cursor.fetchall()
    for item in data:
        id,idnumber,email,password,fname,lname,bday,gender,address,city,country,phone= item
        if idnum==idnumber:
            return True
    return False

# ========================= AdminDashboard Functions ========================= #

# --- [adminlist] --- #
def f_adminlist(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        print(ID)
        admin1 = Admin.objects.filter(id=ID)
        admlist=Admin.objects.all()
        if admin1:
            return render(request, 'admin_templates/adminlist.html', {"admin1":admin1, "admlist":admlist})


def check_admin_idnumber(idnum):
    cursor.execute("SELECT * FROM admin")
    data = cursor.fetchall()
    for item in data:
        id,idnumber,password,fname,lname= item
        if idnum==idnumber:
            return True
    return False

def f_adminadd(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=ID)
        admlist=Admin.objects.all()
        save_record=Admin()
        checker=request.POST.get('idnumber')
        save_record.idnumber=request.POST.get('idnumber')
        save_record.password=request.POST.get('pass')
        save_record.fname=request.POST.get('fname')
        save_record.lname=request.POST.get('lname')
        if admin1:
            if check_admin_idnumber(checker)== True:
                messages.error(request,'This Id Number is already exist!')
                return render(request, 'admin_templates/adminlist.html', {"admin1":admin1, "admlist":admlist})
            save_record.save()
            messages.success(request, 'Admin registered successful!')
            alladmins2=Admin.objects.all()
            return render(request, 'admin_templates/adminlist.html', {"admin1":admin1, "admlist":alladmins2})
    else:
        return login(request)

def f_adminchange(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        print(DID)
        alladmins=Admin.objects.all()
        admin1 = Admin.objects.filter(id=ID)
        IDNUM = request.POST.get('idnumber')
        PASS = request.POST.get('password')
        FN = request.POST.get('fname')
        LN = request.POST.get('lname')
        print(IDNUM)
        if admin1:
            print('=================================================================')
            print(IDNUM)
            Admin.objects.filter(id = DID).update(idnumber=IDNUM)
            Admin.objects.filter(id = DID).update(password=PASS)
            Admin.objects.filter(id = DID).update(fname=FN)
            Admin.objects.filter(id = DID).update(lname=LN)
            print("Update  ok")
            messages.success(request, 'Admin changed successful!')
            alladmins2=Admin.objects.all()
            return render(request, 'admin_templates/adminlist.html', {"admin1":admin1, "admlist":alladmins2})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return render(request, 'admin_templates/adminlist.html', {"admin1":admin1, "admlist":alladmins})



def f_admindelete(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        admin1 = Admin.objects.filter(id=ID)
        alladmins=Admin.objects.all()
        if admin1:
            try:
                admin2 = Admin.objects.get(id = DID)
                admin2.delete()
                print("Delete  ok")
                alladmins2=Admin.objects.all()
                return render(request, 'admin_templates/adminlist.html', {"admin1":admin1, "admlist":alladmins2})
            except:
                print("Not exist")
                return render(request, 'admin_templates/adminlist.html', {"admin1":admin1, "admlist":alladmins})


# --- [workerlist] --- #

def f_workerlist(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        print(ID)
        admin1 = Admin.objects.filter(id=ID)
        wrklist=Worker.objects.all()
        if admin1:
            return render(request, 'admin_templates/workerlist.html', {"admin1":admin1, "wrklist":wrklist})


def check_worker_idnumber(idnum):
    cursor.execute("SELECT * FROM worker")
    data = cursor.fetchall()
    for item in data:
        id,idnumber,password,fname,lname= item
        if idnum==idnumber:
            return True
    return False

def f_workeradd(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=ID)
        wrklist=Worker.objects.all()
        save_record=Worker()
        checker=request.POST.get('idnumber')
        save_record.idnumber=request.POST.get('idnumber')
        save_record.password=request.POST.get('pass')
        save_record.fname=request.POST.get('fname')
        save_record.lname=request.POST.get('lname')
        if admin1:
            if check_worker_idnumber(checker)== True:
                messages.error(request,'This Id Number is already exist!')
                return render(request, 'admin_templates/workerlist.html', {"admin1":admin1, "wrklist":wrklist})
            save_record.save()
            messages.success(request, 'Worker registered successful!')
            wrklist2=Worker.objects.all()
            return render(request, 'admin_templates/workerlist.html', {"admin1":admin1, "wrklist":wrklist2})
    else:
        return login(request)

def f_workerchange(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        print(DID)
        wrklist=Worker.objects.all()
        admin1 = Admin.objects.filter(id=ID)
        IDNUM = request.POST.get('idnumber')
        PASS = request.POST.get('password')
        FN = request.POST.get('fname')
        LN = request.POST.get('lname')
        print(IDNUM)
        if admin1:
            print('=================================================================')
            print(IDNUM)
            Worker.objects.filter(id = DID).update(idnumber=IDNUM)
            Worker.objects.filter(id = DID).update(password=PASS)
            Worker.objects.filter(id = DID).update(fname=FN)
            Worker.objects.filter(id = DID).update(lname=LN)
            print("Update  ok")
            messages.success(request, 'Worker changed successful!')
            wrklist2=Worker.objects.all()
            return render(request, 'admin_templates/workerlist.html', {"admin1":admin1, "wrklist":wrklist2})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return render(request, 'admin_templates/workerlist.html', {"admin1":admin1, "wrklist":wrklist})



def f_workerdelete(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        admin1 = Admin.objects.filter(id=ID)
        wrklist=Worker.objects.all()
        if admin1:
            try:
                worker1 = Worker.objects.get(id = DID)
                worker1.delete()
                print("Delete  ok")
                wrklist2=Worker.objects.all()
                return render(request, 'admin_templates/workerlist.html', {"admin1":admin1, "wrklist":wrklist2})
            except:
                print("Not exist")
                return render(request, 'admin_templates/workerlist.html', {"admin1":admin1, "wrklist":wrklist})

# --- [clientlist] --- #

def f_clientlist(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        print(ID)
        admin1 = Admin.objects.filter(id=ID)
        cltlist=Client.objects.all()
        if admin1:
            return render(request, 'admin_templates/clientlist.html', {"admin1":admin1, "cltlist":cltlist})

def f_clientadd(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=ID)
        cltlist=Client.objects.all()
        save_record=Client()
        checker=request.POST.get('idnumber')
        save_record.idnumber=request.POST.get('idnumber')
        save_record.email=request.POST.get('email')
        save_record.password=request.POST.get('pass')
        save_record.fname=request.POST.get('fname')
        save_record.lname=request.POST.get('lname')
        save_record.bday=request.POST.get('bday')
        save_record.gender=request.POST.get('gender')
        save_record.address=request.POST.get('address')
        save_record.city=request.POST.get('city')
        save_record.country=request.POST.get('country')
        save_record.phone=request.POST.get('phone')
        if admin1:
            if check_client_idnumber(checker)== True:
                messages.error(request,'This Id Number is already exist!')
                return render(request, 'admin_templates/clientlist.html', {"admin1":admin1, "cltlist":cltlist})
            save_record.save()
            messages.success(request, 'Worker registered successful!')
            cltlist2=Client.objects.all()
            return render(request, 'admin_templates/clientlist.html', {"admin1":admin1, "cltlist":cltlist2})
    else:
        return login(request)

def f_clientchange(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        print(DID)
        cltlist=Client.objects.all()
        admin1 = Admin.objects.filter(id=ID)
        IDNUM = request.POST.get('idnumber')
        PASS = request.POST.get('password')
        FN = request.POST.get('fname')
        LN = request.POST.get('lname')
        EMAIL = request.POST.get('email')
        BDAY = request.POST.get('bday')
        GENDER=request.POST.get('gender')
        ADDRESS=request.POST.get('address')
        CITY=request.POST.get('city')
        COUNTRY=request.POST.get('country')
        PHONE=request.POST.get('phone')
        if admin1:
            print('=================================================================')
            print(IDNUM)
            Client.objects.filter(id = DID).update(idnumber=IDNUM)
            Client.objects.filter(id = DID).update(password=PASS)
            Client.objects.filter(id = DID).update(fname=FN)
            Client.objects.filter(id = DID).update(lname=LN)
            Client.objects.filter(id = DID).update(email=EMAIL)
            Client.objects.filter(id = DID).update(bday=BDAY)
            Client.objects.filter(id = DID).update(gender=GENDER)
            Client.objects.filter(id = DID).update(address=ADDRESS)
            Client.objects.filter(id = DID).update(city=CITY)
            Client.objects.filter(id = DID).update(country=COUNTRY)
            Client.objects.filter(id = DID).update(phone=PHONE)
            print("Update  ok")
            messages.success(request, 'Client changed successful!')
            cltlist2=Client.objects.all()
            return render(request, 'admin_templates/clientlist.html', {"admin1":admin1, "cltlist":cltlist2})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return render(request, 'admin_templates/clientlist.html', {"admin1":admin1, "cltlist":cltlist})



def f_clientdelete(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        admin1 = Admin.objects.filter(id=ID)
        cltlist=Client.objects.all()
        if admin1:
            try:
                worker1 = Client.objects.get(id = DID)
                worker1.delete()
                print("Delete  ok")
                cltlist2=Client.objects.all()
                return render(request, 'admin_templates/clientlist.html', {"admin1":admin1, "cltlist":cltlist2})
            except:
                print("Not exist")
                return render(request, 'admin_templates/clientlist.html', {"admin1":admin1, "cltlist":cltlist})

# ========================= WorkerDashboard Functions ========================= #

# ========================= ClientDashboard Functions ========================= #

# --- [client profil] --- #

def f_clientinfo1(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        client1 = Client.objects.filter(id=DID)
        FN = request.POST.get('fname')
        LN = request.POST.get('lname')
        EMAIL = request.POST.get('email')
        BDAY = request.POST.get('bday')
        GENDER=request.POST.get('gender')
        ADDRESS=request.POST.get('address')
        CITY=request.POST.get('city')
        COUNTRY=request.POST.get('country')
        PHONE=request.POST.get('phone')
        if client1:
            Client.objects.filter(id = DID).update(fname=FN)
            Client.objects.filter(id = DID).update(lname=LN)
            Client.objects.filter(id = DID).update(email=EMAIL)
            Client.objects.filter(id = DID).update(bday=BDAY)
            Client.objects.filter(id = DID).update(gender=GENDER)
            Client.objects.filter(id = DID).update(address=ADDRESS)
            Client.objects.filter(id = DID).update(city=CITY)
            Client.objects.filter(id = DID).update(country=COUNTRY)
            Client.objects.filter(id = DID).update(phone=PHONE)
            messages.success(request, 'Client information changed successfully!')
            return render(request, 'client_templates/profil.html', {"client1":client1})
    else:
        return login(request)

def f_clientinfo2(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        client1 = Client.objects.filter(id=DID)
        PW = request.POST.get('password')
        if client1:
            Client.objects.filter(id = DID).update(password=PW)
            messages.success(request, 'Client password changed successfully!')
            return render(request, 'client_templates/profil.html', {"client1":client1})
    else:
        return login(request)

# --- [client navigation] --- #

def f_nav_shop(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        client1 = Client.objects.filter(id=DID)
        if client1:
            return render(request, 'client_templates/index.html', {"client1":client1})

def f_nav_profil(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        client1 = Client.objects.filter(id=DID)
        if client1:
            return render(request, 'client_templates/profil.html', {"client1":client1})




