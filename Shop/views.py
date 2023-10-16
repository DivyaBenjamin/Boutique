from django.shortcuts import render,redirect
from Shop import *
# Create your views here.
def shopboutique(request):
    return render(request,'Shop/Home.html')