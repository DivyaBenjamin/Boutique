from django.shortcuts import redirect,render
from Admin.models import *
from Shop.models import *
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

def shopreg(request):
    shopdata=tbl_shop.objects.all()
    if request.method=="POST":
        tbl_shop.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),email=request.POST.get('email'),phone=request.POST.get('phoneNumber'),password=request.POST.get('password'),image=request.FILES.get('shopimg'),proof=request.FILES.get('proof'))
        return redirect('adminboutique:shopreg')
    else:
        return render(request,'Admin/Shopreg.html',{'data':shopdata})

def haircuts(request):
    haircutdata=tbl_haircuts.objects.all()
    if request.method=="POST":
        tbl_haircuts.objects.create(haircuts=request.POST.get('haircuts'))
        return redirect('adminboutique:haircuts')
    else:
        return render(request,'Admin/Haircuts.html',{'haircuts':haircutdata})

def deletehair(request,cid):
    tbl_haircuts.objects.get(id=cid).delete()
    return redirect('adminboutique:haircuts')

def typesofhaircut(request):
    haircutdata=tbl_haircuts.objects.all()
    typesofhair=tbl_typesofhair.objects.all()
    if request.method=="POST":
        haircuts=tbl_haircuts.objects.get(id=request.POST.get('haircuts'))
        tbl_typesofhair.objects.create(typesofhair=request.POST.get('typesofhair'),haircuts=haircuts)
        return redirect('adminboutique:typesofhaircut')
    else:
        return render(request,'Admin/Typesofhaircut.html',{'haircuts':haircutdata,'typeshair':typesofhair})

def deletetypeshair(request,did):
    tbl_typesofhair.objects.get(id=did).delete()
    return redirect('adminboutique:typesofhaircut')

def adminreg(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        tbl_admin.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),email=request.POST.get('email'),phone=request.POST.get('phoneNumber'),password=request.POST.get('password'),gender=request.POST.get('gender'))
        return redirect('adminboutique:adminreg')
    else:
        return render(request,'Admin/Adminreg.html',{'data':data})
