from django.shortcuts import redirect,render
from Admin.models import *
# Create your views here.
def adminboutique(request):
    return render(request,'Admin/home.html')

def userreg(request):
    data=tbl_user.objects.all()
    if request.method=="POST":
        tbl_user.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),email=request.POST.get('email'),phone=request.POST.get('phoneNumber'),password=request.POST.get('password'),gender=request.POST.get('gender'))
        return redirect('adminboutique:userreg')
    else:
        return render(request,'Admin/Userreg.html',{'data':data})

def staffreg(request):
    if request.method=="POST":
        tbl_staff.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),email=request.POST.get('email'),phone=request.POST.get('phoneNumber'),password=request.POST.get('password'),gender=request.POST.get('gender'),dateoj=request.POST.get('dateofjoining'))
        return redirect('adminboutique:staffreg')
    else:
        return render(request,'Admin/Staffreg.html')