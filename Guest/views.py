from django.shortcuts import render,redirect
from Admin.models import*

# Create your views here.
def login(request):
    return render(request,'Guest/Login.html')
