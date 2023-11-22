from django.shortcuts import redirect,render
from Admin.models import *
from Shop.models import *
from Userboutique.models import *
# Create your views here.
def adminboutique(request):
    return render(request,'Admin/home.html')

def staffreg(request):
    staffdata=tbl_staffreg.objects.all()
    if request.method=="POST":
        tbl_staffreg.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),phone=request.POST.get('phoneNumber'),email=request.POST.get('email'),gender=request.POST.get('gender'),password=request.POST.get('password'),doj=request.POST.get('dateofjoining'),image=request.FILES.get('img'),photo=request.FILES.get('proof'))
        return redirect('adminboutique:staffreg')
    else:
        return render(request,'Admin/Staffreg.html',{'data':staffdata})

def servicestypes(request):
    servicesdata=tbl_typesofservices.objects.all()
    if request.method=="POST":
        tbl_typesofservices.objects.create(servicestypes=request.POST.get('services'))
        return redirect('adminboutique:servicestypes')
    else:
        return render(request,'Admin/Servicetype.html',{'services':servicesdata})

def deleteservices(request,bid):
    tbl_typesofservices.objects.get(id=bid).delete()
    return redirect('adminboutique:servicestypes')

def addservices(request):
    servicesdata=tbl_typesofservices.objects.all()
    addservicesdata=tbl_addservices.objects.all()
    if request.method=="POST":
        typesofservice=tbl_typesofservices.objects.get(id=request.POST.get('servicestypes'))
        tbl_addservices.objects.create(servicesdetail=request.POST.get('servicesdetail'),rate=request.POST.get('rate'),image=request.FILES.get('image'),servicestypes=typesofservice)
        return redirect('adminboutique:addservices')
    else:
        return render(request,'Admin/Addservices.html',{'services':servicesdata,'addservice':addservicesdata})

def deleteaddservice(request,cid):
    tbl_addservices.objects.get(id=cid).delete()
    return redirect('adminboutique:addservices')

def work(request):
    workdata=tbl_workgalary.objects.all()
    if request.method=="POST":
        tbl_workgalary.objects.create(caption=request.POST.get('caption'),image=request.FILES.get('image'))
        return redirect('adminboutique:work')
    else:
        return render(request,'Admin/Workgalary.html',{'work':workdata})

def deletework(request,aid):
    tbl_workgalary.objects.get(id=aid).delete()
    return redirect('adminboutique:work')

def adminreg(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        tbl_admin.objects.create(name=request.POST.get('fullName'),username=request.POST.get('username'),email=request.POST.get('email'),phone=request.POST.get('phoneNumber'),password=request.POST.get('password'),gender=request.POST.get('gender'))
        return redirect('adminboutique:adminreg')
    else:
        return render(request,'Admin/Adminreg.html',{'data':data})


def stafflist(request,eid):
    stf_data=tbl_staffreg.objects.all()
    bookingdata=tbl_bookingservice.objects.get(id=eid)
    bid=bookingdata.id
    request.session["bkid"]=bid
    return render(request,'Admin/Assignstaff.html',{'stf_data':stf_data})



def assignstaff(request,did):
    bdata=tbl_bookingservice.objects.get(id=request.session["bkid"])
    bdata.booking_status=1
    bdata.save()
    vid=bdata.id
    stfdata=tbl_staffreg.objects.get(id=did)
    tbl_assignstaff.objects.create(assign_status=1,staff=stfdata,booking=bdata)
    return redirect('adminboutique:viewbooking')
    

def viewfeedback(request):
    user=tbl_user.objects.all()
    userdata=tbl_feedback.objects.filter(user_id__in=user)
    return render(request,'Admin/Viewfeedback.html',{'feedback':userdata})

def viewbooking(request):
    bookingdata=tbl_bookingservice.objects.all()
    return render(request,'Admin/Viewbooking.html',{'bookingservice':bookingdata})

def assignwork(request):
    booking=tbl_bookingservice.objects.all()
    assigndata=tbl_assignstaff.objects.filter(assign_status=1)
    return render(request,'Admin/Assignwork.html',{'assignstaff':assigndata})