from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
from BeSce.models import Client
from BeSce.models import Pharmacian
from BeSce.models import Director

def index(request):
    return render(request,'index.html')