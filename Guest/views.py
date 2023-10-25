from django.shortcuts import render,redirect
from Admin.models import*

# Create your views here.
def login(request):
    if request.method=="POST":
        usercount=tbl_user.objects.filter(email=request.POST.get('email'),password=request.POST.get('password')).count()
        shopcount=tbl_staff.objects.filter(email=request.POST.get('email'),password=request.POST.get('password')).count()
        if usercount>0:
            userdata=tbl_user.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
            request.session["uid"]=userdata.id
            request.session["uname"]=userdata.name
            return redirect('Userboutique:Userboutique')
        elif shopcount>0:
            shopdata=tbl_staff.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
            request.session["sid"]=shopdata.id
            request.session["sname"]=shopdata.name
            return redirect('shopboutique:shopboutique')
        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,'Guest/Login.html')
