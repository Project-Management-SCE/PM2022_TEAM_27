from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
import requests
from BeSce.models import Client, Ordered, Prescription, Worker, Admin
from BeSce.models import Product, Ordershop
# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="db_besce")

'''
db_connection = mysql.connector.connect(
  host="database-1.c4joaqwcqrpg.eu-central-1.rds.amazonaws.com",
  user="admin",
  password="okoklol123",
  database="db_besce")
'''

cursor = db_connection.cursor()
print(db_connection)

# ====================|All Views Functions|==================== #
'''
products_name = [
    "Acamol"

]
context_api = []
for prod in products_name:
    path = "https://api.fda.gov/drug/label.json?search=" + prod
    response = requests.get(path)
    js = response.json()["results"]
    context_prod = js[0]
    WARNINGS = ""
    if 'description' in context_prod:
        WARNINGS = context_prod["description"]
    context_api += WARNINGS
'''

# ============================================================= #

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


def clin(request):
    return render(request, 'client_templates/index.html')

def clmyor(request):
    return render(request,'client_templates/myorder.html')

def clpay(request):
    return render(request,'client_templates/payment.html')

def clpayok(request):
    return render(request,'client_templates/paymentok.html')

def clpro(request):
    return render(request,'client_templates/profil.html')

def wkin(request):
    return render(request,'worker_templates/index.html')

def wkkkpr(request):
    return render(request,'worker_templates/kkprlist.html')

def wkneor(request):
    return render(request,'worker_templates/neworder.html')

def wkmyor(request):
    return render(request,'worker_templates/wkmyorders.html')

def adin(request):
    return render(request,'admin_templates/index.html')

def adadlt(request):
    return render(request,'admin_templates/adminlist.html')

def adcllt(request):
    return render(request,'admin_templates/clientlist.html')

def adorlt(request):
    return render(request,'admin_templates/orderlist.html')

def adorzlt(request):
    return render(request,'admin_templates/orderzlist.html')

def adprlt(request):
    return render(request,'admin_templates/prescriptionlist.html')

def adprdlt(request):
    return render(request,'admin_templates/productlist.html')

def adwklt(request):
    return render(request,'admin_templates/workerlist.html')


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

# ============================================================================================================================================================= #
# ================================================================= AdminDashboard Functions ================================================================= #
# ============================================================================================================================================================= #

def f_prescriptionlist(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        print(ID)
        admin1 = Admin.objects.filter(id=ID)
        prlist=Prescription.objects.all()
        prdlist=Product.objects.all()
        if admin1:
            return render(request, 'admin_templates/prescriptionlist.html', {"admin1":admin1, "prlst":prlist, "prdlst":prdlist})

def f_prescriptionadd(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=ID)
        prdlist=Product.objects.all()
        save_record=Prescription()
        save_record.pid=request.POST.get('pid')
        save_record.informations=request.POST.get('informations')
        if admin1:
            save_record.save()
            messages.success(request, 'Prescription registered successful!')
            prlist2=Product.objects.all()
            return render(request, 'admin_templates/prescriptionlist.html', {"admin1":admin1, "prdlst":prdlist, "prlst":prlist2})
    else:
        return login(request)

def f_praddclient(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        print(DID)
        admin1 = Admin.objects.filter(id=ID)
        prdlist=Product.objects.all()
        CL = request.POST.get('cid')
        if admin1:
            print('=================================================================')
            Prescription.objects.filter(id = DID).update(cid=CL)
            print("Update  ok")
            messages.success(request, 'Client changed successful!')
            prlist2=Prescription.objects.all()
            return render(request, 'admin_templates/prescriptionlist.html', {"admin1":admin1, "prlst":prlist2, "prdlst":prdlist})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return login(request)

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




# --- [admin navigation] --- #

def f_nav_home_admin(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=DID)
        if admin1:
            return render(request, 'admin_templates/index.html', {"admin1":admin1})

def f_nav_order_admin(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=DID)
        orderslist = Ordered.objects.all()
        clt = Client.objects.all()
        print(orderslist)
        if admin1:
            return render(request, 'admin_templates/orderzlist.html', {"admin1":admin1, "ordlst1":orderslist, "clt":clt})


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

# --- [productlist] --- #
def f_productlist(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=ID)
        prdlist=Product.objects.all()
        if admin1:
            return render(request, 'admin_templates/productlist.html', {"admin1":admin1, "prdlist":prdlist})

def f_productadd(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        admin1 = Admin.objects.filter(id=ID)
        save_record=Product()
        save_record.name=request.POST.get('name')
        save_record.supplier=request.POST.get('supplier')
        save_record.type=request.POST.get('type')
        save_record.price=request.POST.get('price')
        save_record.prescription=request.POST.get('prescription')
        save_record.stock=0
        if admin1:
            save_record.save()
            messages.success(request, 'Product registered successful!')
            prdlist2=Product.objects.all()
            return render(request, 'admin_templates/productlist.html', {"admin1":admin1, "prdlist":prdlist2})
    else:
        return login(request)

def f_productdelete(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        admin1 = Admin.objects.filter(id=ID)
        prdlist=Product.objects.all()
        if admin1:
            try:
                product1 = Product.objects.get(id = DID)
                product1.delete()
                print("Delete  ok")
                prdlist2=Product.objects.all()
                return render(request, 'admin_templates/productlist.html', {"admin1":admin1, "prdlist":prdlist2})
            except:
                print("Not exist")
                return render(request, 'admin_templates/productlist.html', {"admin1":admin1, "prdlist":prdlist})

def f_feelstock(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        admin1 = Admin.objects.filter(id=ID)
        prdlist=Product.objects.all()
        STOCK = request.POST.get('stock')
        if admin1:
            try:
                Product.objects.filter(id = DID).update(stock=STOCK)
                print("Stock Filled")
                prdlist2=Product.objects.all()
                return render(request, 'admin_templates/productlist.html', {"admin1":admin1, "prdlist":prdlist2})
            except:
                print("Not exist")
                return render(request, 'admin_templates/productlist.html', {"admin1":admin1, "prdlist":prdlist})

# ============================================================================================================================================================= #
# ================================================================= WorkerDashboard Functions ================================================================= #
# ============================================================================================================================================================= #

def f_workerindex(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        worker1 = Worker.objects.filter(id=ID)
        if worker1:
            return render(request, 'worker_templates/index.html', {"worker1":worker1})

def f_wkneworder(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        worker1 = Worker.objects.filter(id=DID)
        orderslist = Ordered.objects.all()
        prdlist=Product.objects.all()
        print(orderslist)
        if worker1:
            return render(request, 'worker_templates/neworder.html', {"worker1":worker1, "ordlst1":orderslist})

def f_wkmyorder(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        worker1 = Worker.objects.filter(id=DID)
        orderslist = Ordered.objects.all()
        prdlist=Product.objects.all()
        print(orderslist)
        if worker1:
            return render(request, 'worker_templates/wkmyorders.html', {"worker1":worker1, "ordlst1":orderslist})

def f_takeorder(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        orderslist = Ordered.objects.all()
        worker1 = Worker.objects.filter(id=ID)
        if worker1:
            print('=================================================================')
            Ordered.objects.filter(id = DID).update(wid=ID)
            print("Update  ok")
            messages.success(request, 'Order attribution changed successful!')
            orderslist2 = Ordered.objects.all()
            return render(request, 'worker_templates/neworder.html', {"worker1":worker1, "ordlst1":orderslist2})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return render(request, 'worker_templates/neworder.html', {"worker1":worker1, "ordlst1":orderslist})

def f_finishorder(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        orderslist = Ordered.objects.all()
        worker1 = Worker.objects.filter(id=ID)
        if worker1:
            print('=================================================================')
            Ordered.objects.filter(id = DID).update(status="Completed")
            print("Update  ok")
            messages.success(request, 'Order status changed successful!')
            orderslist2 = Ordered.objects.all()
            return render(request, 'worker_templates/wkmyorders.html', {"worker1":worker1, "ordlst1":orderslist2})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return render(request, 'worker_templates/wkmyorders.html', {"worker1":worker1, "ordlst1":orderslist})

def f_cancelorder(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        orderslist = Ordered.objects.all()
        worker1 = Worker.objects.filter(id=ID)
        if worker1:
            print('=================================================================')
            Ordered.objects.filter(id = DID).update(status="Cancelled")
            print("Update  ok")
            messages.success(request, 'Order status changed successful!')
            orderslist2 = Ordered.objects.all()
            return render(request, 'worker_templates/wkmyorders.html', {"worker1":worker1, "ordlst1":orderslist2})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return render(request, 'worker_templates/wkmyorders.html', {"worker1":worker1, "ordlst1":orderslist})

def f_praddnewclient(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        DID= request.POST.get('did')
        print(DID)
        worker1 = Worker.objects.filter(id=ID)
        CL = request.POST.get('cid')
        if worker1:
            print('=================================================================')
            Prescription.objects.filter(id = DID).update(cid=CL)
            print("Update  ok")
            messages.success(request, 'Client changed successful!')
            prlist2=Prescription.objects.all()
            return render(request, 'worker_templates/kkprlist.html', {"worker1":worker1, "prlist":prlist2})
        else:
            print("Not exist")
            messages.error(request,'Error!')
            return login(request)

def f_wkprlist(request):
    if request.method == 'POST':
        ID= request.POST.get('id')
        print(ID)
        worker1 = Worker.objects.filter(id=ID)
        prlist=Prescription.objects.all()
        if worker1:
            return render(request, 'worker_templates/kkprlist.html', {"worker1":worker1, "prlist":prlist})

# ============================================================================================================================================================= #
# ================================================================= ClientDashboard Functions ================================================================= #
# ============================================================================================================================================================= #

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
        prdlist=Product.objects.all()
        cl1order = Ordershop.objects.filter(cid=DID)
        if client1:
            return render(request, 'client_templates/index.html', {"client1":client1, "prdlist":prdlist, "cl1order":cl1order})

def f_nav_ordershop(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        client1 = Client.objects.filter(id=DID)
        cl1order = Ordershop.objects.filter(cid=DID)
        prdlist = Product.objects.all()
        if client1:
            return render(request, 'client_templates/myorder.html', {"client1":client1, "cl1order":cl1order, "prdlist":prdlist})

def f_nav_profil(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        client1 = Client.objects.filter(id=DID)
        orderslist1 = Ordered.objects.all()
        prdlist = Product.objects.all()
        if client1:
            return render(request, 'client_templates/profil.html', {"client1":client1, "ordlst1":orderslist1, "prdlist":prdlist})

# --- [client navigation] --- #
def f_payment(request):
    if request.method=='POST':
        DID= request.POST.get('id')
        client1 = Client.objects.filter(id=DID)
        if client1:
            return render(request, 'client_templates/payment.html', {"client1":client1})


def f_paymentok(request):
    if request.method=='POST':
        price = 0
        oc = []
        qc = []
        ID= request.POST.get('id')
        client1 = Client.objects.filter(id=ID)
        clientordershop = Ordershop.objects.filter(cid=ID)
        cl1order = Ordershop.objects.filter(cid=ID)
        prdlist = Product.objects.all()
        if client1:
            save_record=Ordered()
            save_record.status='Waiting'
            save_record.cid=ID
            for ord1 in clientordershop:
                PID = ord1.pid
                actualprod = Product.objects.filter(id = PID).first()
                if oc is None:
                    oc.append(actualprod.name)
                else:
                    oc.append('/' + actualprod.name)
                if qc is None:
                    qc.append(str(ord1.quantity))
                else:
                    qc.append('/' + str(ord1.quantity))    
                price = price + actualprod.price
                stk = actualprod.stock - ord1.quantity
                if stk < 0:
                    messages.error(request, 'Empty stock for the product ' + actualprod.name)
                    Ordershop.objects.filter(cid = ID, pid = PID).delete()
                    return render(request, 'client_templates/index.html', {"client1":client1, "prdlist":prdlist, "cl1order":cl1order})
                Product.objects.filter(id = PID).update(stock=stk)
            save_record.total = price
            save_record.pid = oc
            save_record.quantity = qc
            save_record.save()
            clientordershop.delete()
            return render(request, 'client_templates/paymentok.html', {"client1":client1})




def f_addactualorder(request):
    if request.method=='POST':
        CID= request.POST.get('id')
        DID = request.POST.get('did')
        print(CID , DID)
        client1 = Client.objects.filter(id=CID)
        prdlist=Product.objects.all()
        ordlist=Ordershop.objects.all()
        cl1order = Ordershop.objects.filter(cid=CID)
        if client1:
            prdexist = Ordershop.objects.filter(cid = CID, pid = DID).first()
            if prdexist:
               
                print(prdexist)
                QTT = prdexist.quantity
                QTT = QTT+ 1
                Ordershop.objects.filter(cid = CID, pid = DID).update(quantity = QTT)

            
            else:
                save_record=Ordershop()
                save_record.cid=request.POST.get('id')
                save_record.pid=request.POST.get('did')
                save_record.quantity=1
                save_record.save()
            
            cl1order2 = Ordershop.objects.filter(cid=CID)
            return render(request, 'client_templates/index.html', {"client1":client1, "prdlist":prdlist, "cl1order":cl1order2})

def f_delactualorder(request):
    if request.method=='POST':
        CID= request.POST.get('id')
        DID = request.POST.get('did')
        print(CID , DID)
        client1 = Client.objects.filter(id=CID)
        prdlist=Product.objects.all()
        cl1order = Ordershop.objects.filter(cid=CID)
        if client1:
            Ordershop.objects.filter(cid = CID, pid = DID).delete()
            cl1order2 = Ordershop.objects.filter(cid=CID)
            return render(request, 'client_templates/myorder.html', {"client1":client1, "prdlist":prdlist, "cl1order":cl1order2})
        else:
            return render(request, 'client_templates/myorder.html', {"client1":client1, "prdlist":prdlist, "cl1order":cl1order})

