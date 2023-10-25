from django.shortcuts import render,redirect
from Shop.models import *
from Admin.models import *
# Create your views here.
def shopboutique(request):
    return render(request,'Shop/Home.html')

def addingstyles(request):
    stylesdata=tbl_styles.objects.all()
    typesofstyledata=tbl_typesof.objects.all()
    if request.method=="POST":
        sty=tbl_styles.objects.get(id=request.POST.get('Styles'))
        typesof=tbl_typesof.objects.get(id=request.POST.get('typesof'))
        tbl_addingstyles.objects.create(name=request.POST.get('name'),rate=request.POST.get('rate'),image=request.FILES.get('image'),typesof=typesof)
        return render(request,'Shop/Addingstyles.html')
    else:
        return render(request,'Shop/Addingstyles.html',{'sty':stylesdata,'typesof':typesofstyledata})

def Ajaxstyles(request):
    styles=tbl_styles.objects.get(id=request.GET.get('pisd'))
    typesofstyle=tbl_typesof.objects.filter(styles=styles)
    return render(request,'Shop/Ajaxstyles.html',{'typesof':typesofstyle})

def staffreg(request):
    staffdata=tbl_staff.objects.all()
    if request.method=="POST":
        tbl_staff.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),email=request.POST.get('email'),phone=request.POST.get('phoneNumber'),password=request.POST.get('password'),gender=request.POST.get('gender'),dateoj=request.POST.get('dateofjoining'))
        return redirect('shopboutique:staffreg')
    else:
        return render(request,'Shop/Staffreg.html',{'data':staffdata})

def addinghair(request):
    return render(request,'Shop/Addinghair.html')

def Ajaxcut(request):
    return render(request,'Shop/Ajaxcut.html')