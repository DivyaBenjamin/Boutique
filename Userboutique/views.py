from django.shortcuts import render,redirect
from Userboutique.models import *

# Create your views here.
def Userboutique(request):
    return render(request,'Userboutique/home.html')

def styles(request):
    return render(request,'Userboutique/Styles.html')