from django.shortcuts import redirect,render
from Guest.models import *
from Admin.models import *


# Create your views here.
def login(request):
    if request.method=="POST":
        usercount=tbl_user.objects.filter(email=request.POST.get('email'),password=request.POST.get('password')).count()
        staffcount=tbl_staffreg.objects.filter(email=request.POST.get('email'),password=request.POST.get('password')).count()
        admincount=tbl_admin.objects.filter(email=request.POST.get('email'),password=request.POST.get('password')).count()
        if usercount>0:
            userdata=tbl_user.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
            request.session["uid"]=userdata.id
            request.session["uname"]=userdata.name
            return redirect('Userboutique:Userboutique')
        elif staffcount>0:
            staffdata=tbl_staffreg.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
            request.session["sid"]=staffdata.id
            request.session["sname"]=staffdata.name
            return redirect('shopboutique:shopboutique')
        elif admincount>0:
            admindata=tbl_admin.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
            request.session["aid"]=admindata.id
            request.session["aname"]=admindata.name
            return redirect('adminboutique:adminboutique')
        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,'Guest/Login.html')

def userreg(request):
    userdata=tbl_user.objects.all()
    if request.method=="POST":
        tbl_user.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),phone=request.POST.get('phoneNumber'),email=request.POST.get('email'),gender=request.POST.get('gender'),password=request.POST.get('password'),image=request.FILES.get('image'))
        return redirect('webguest:userreg')
    else:
        return render(request,'Guest/Userreg.html',{'data':userdata})
