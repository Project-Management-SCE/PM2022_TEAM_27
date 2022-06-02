from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # --- [Main] --- #
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('FirstTimePage/', views.FirstTimePage, name='FirstTimePage'),
    path('client_registration/', views.client_registration, name='client_registration'),
    path('f_register', views.f_register),
    path('f_login', views.f_login),
    path('clientDashboard/', views.ClientDashboard, name='clientDashboard'),

    # --- [Admin - admin] --- #
    path('adminlist', views.f_adminlist, name='adminlist'),
    path('admindelete', views.f_admindelete),
    path('addadmin', views.f_adminadd),
    path('adminchange', views.f_adminchange),
    path('admin_index', views.f_nav_home_admin),

    # --- [Admin - worker] --- #
    path('workerlist', views.f_workerlist, name='workerlist'),
    path('workerdelete', views.f_workerdelete),
    path('addworker', views.f_workeradd),
    path('workerchange', views.f_workerchange),

    # --- [Admin - client] --- #
    path('clientlist', views.f_clientlist, name='clientlist'),
    path('clientdelete', views.f_clientdelete),
    path('addclient', views.f_clientadd),
    path('clientchange', views.f_clientchange),

    # --- [Admin - product] --- #
    path('productlist', views.f_productlist),
    path('addproduct', views.f_productadd),
    path('deleteproduct', views.f_productdelete),
    path('feelstock', views.f_feelstock),

    # --- [Admin - order] --- #
    path('orderlist', views.f_nav_order_admin),

    # --- [Admin - prescriptions] --- #
    path('prescriptionlist', views.f_prescriptionlist),
    path('addprescription', views.f_prescriptionadd),
    path('praddclient', views.f_praddclient),

    # --- [Client - Profil] --- #
    path('clientinfo1', views.f_clientinfo1),
    path('clientinfo2', views.f_clientinfo2),

    # --- [Client - Nav] --- #
    path('nav_shop', views.f_nav_shop),
    path('nav_profil', views.f_nav_profil),

    # --- [Client - OrderShop] --- #
    path('addtoorder', views.f_addactualorder),
    path('deltoorder', views.f_delactualorder),
    path('myorder', views.f_nav_ordershop),
    path('payment', views.f_payment),
    path('paymentok', views.f_paymentok),

    # --- [Worker - navfunc] --- #
    path('workerindex', views.f_workerindex),
    path('wkneworder', views.f_wkneworder),
    path('takeorder', views.f_takeorder),
    path('wkorder', views.f_wkmyorder),
    path('finishorder', views.f_finishorder),
    path('cancelorder', views.f_cancelorder),
    path('praddnewclient', views.f_praddnewclient),
    path('wkprlist', views.f_wkprlist),

    # --- [TEST URLS] --- #
    path('clin', views.clin, name='clin'),
    path('clmyor', views.clmyor, name='clmyor'),
    path('clpay', views.clpay, name='clpay'),
    path('clpayok', views.clpayok, name='clpayok'),
    path('clpro', views.clpro, name='clpro'),

    path('wkin', views.wkin, name='wkin'),
    path('wkkkpr', views.wkkkpr, name='wkkkpr'),
    path('wkneor', views.wkneor, name='wkneor'),
    path('wkmyor', views.wkmyor, name='wkmyor'),

    path('adin', views.adin, name='adin'),
    path('adadlt', views.adadlt, name='adadlt'),
    path('adcllt', views.adcllt, name='adcllt'),
    path('adorlt', views.adorlt, name='adorlt'),
    path('adorzlt', views.adorzlt, name='adorzlt'),
    path('adprdlt', views.adprdlt, name='adprdlt'),
    path('adwklt', views.adwklt, name='adwklt'),
    path('adprlt', views.adprlt, name='adprlt'),

    ]