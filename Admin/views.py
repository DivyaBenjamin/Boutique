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
    staffdata=tbl_staff.objects.all()
    if request.method=="POST":
        tbl_staff.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),email=request.POST.get('email'),phone=request.POST.get('phoneNumber'),password=request.POST.get('password'),gender=request.POST.get('gender'),dateoj=request.POST.get('dateofjoining'))
        return redirect('adminboutique:staffreg')
    else:
        return render(request,'Admin/Staffreg.html',{'data':staffdata})

def styles(request):
    stylesdata=tbl_styles.objects.all()
    if request.method=="POST":
        tbl_styles.objects.create(styles=request.POST.get('styles'))
        return redirect('adminboutique:styles')
    else:
        return render(request,'Admin/Styles.html',{'sty':stylesdata})

def deletesty(request,aid):
    tbl_styles.objects.get(id=aid).delete()
    return redirect('adminboutique:styles')

def typesofstyle(request):
    stylesdata=tbl_styles.objects.all()
    typesofstyledata=tbl_typesof.objects.all()
    if request.method=="POST":
        sty=tbl_styles.objects.get(id=request.POST.get('Styles'))
        tbl_typesof.objects.create(typesof=request.POST.get('typesofstyles'),styles=sty)
        return redirect('adminboutique:typesofstyle')
    else:
        return render(request,'Admin/Typesofstyle.html',{'sty':stylesdata,'typesof':typesofstyledata})

def deletetypesof(request,bid):
    tbl_typesof.objects.get(id=bid).delete()
    return redirect('adminboutique:typeofstyle')

