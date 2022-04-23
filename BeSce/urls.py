from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # --- [Main] --- #
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('FirstTimePage/', views.FirstTimePage, name='FirstTimePage'),
    path('client_registration/', views.client_registration, name='client_registration'),
    path('f_register', views.f_register),
    path('index/', views.ClientIndex, name='index'),
    path('f_login', views.f_login),
    path('clientDashboard/', views.ClientDashboard, name='clientDashboard'),
    # --- [Admin - admin] --- #
    path('adminlist', views.f_adminlist, name='adminlist'),
    path('admindelete', views.f_admindelete),
    path('addadmin', views.f_adminadd),
    path('adminchange', views.f_adminchange),
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
    path('ClientProfil', views.ClientProfil),
    # --- [Client - Profil] --- #
    path('clientinfo1', views.f_clientinfo1),
    path('clientinfo2', views.f_clientinfo2),
    # --- [Client - Nav] --- #
    path('nav_shop', views.f_nav_shop),
    path('nav_profil', views.f_nav_profil),
    ]