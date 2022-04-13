from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('FirstTimePage', views.FirstTimePage, name='FirstTimePage'),
    path('client_registration', views.client_registration, name='client_registration'),
    path('f_register', views.f_register),
    path('cindex', views.cindex, name='index'),
    path('f_cregister', views.f_cregister),
    path('f_login', views.f_login),
    ]