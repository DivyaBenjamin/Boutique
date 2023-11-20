from django.shortcuts import render,redirect
from Userboutique.models import *
from Guest.models import *
from django.contrib.auth import logout as logouts

# Create your views here.
def Userboutique(request):
    User=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'Userboutique/home.html',{'i':User})

def styles(request):
    stypedata=tbl_typesofservices.objects.all()
    userdata=tbl_user.objects.get(id=request.session["uid"])
    servicesdata=tbl_addservices.objects.all()
    return render(request,'Userboutique/Styles.html',{'servicestypes':stypedata,'services':servicesdata})

def ajaxservice(request):
    types=tbl_typesofservices.objects.get(id=request.GET.get("sid"))
    services=tbl_addservices.objects.filter(servicestypes=types)
    return render(request,"Userboutique/Ajaxservice.html",{'services':services})

def bookingservice(request,pid):
    bookingservicedata=tbl_bookingservice.objects.all()
    userdata=tbl_user.objects.get(id=request.session["uid"])
    serviceid=tbl_addservices.objects.get(id=pid)
    if request.method=="POST":
        tbl_bookingservice.objects.create(booked_date=request.POST.get('Bookeddate'),user=userdata,services=serviceid)
        return redirect('Userboutique:Userboutique')
    else:
        return render(request,'Userboutique/Bookingservice.html',{'err':2})

def about(request):
    return render(request,'Userboutique/About.html')

def blog(request):
    blogdata=tbl_blogs.objects.all()
    if request.method=="POST":
        tbl_blogs.objects.create(subject=request.POST.get('subject'),message=request.POST.get('message'))
        return redirect('Userboutique:blog')
    else:
        return render(request,'Userboutique/Blog.html',{'data':blogdata,'err':1})

def feedback(request):
    feedbackdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        tbl_feedback.objects.create(message=request.POST.get('message'),user=feedbackdata)
        return redirect('Userboutique:feedback')
    else:
        return render(request,'Userboutique/Feedback.html')

def profile(request):
    User=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'Userboutique/Profile.html',{'i':User})

def editprofile(request):
    edituser=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        edituser.name=request.POST.get('name')
        edituser.username=request.POST.get('username')
        edituser.save()
        return redirect('Userboutique:editprofile')
    else:
        return render(request,'Userboutique/Editprofile.html',{'i':edituser})

def changepassword(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        if (user.password)==(request.POST.get('currentpassword')):
            if (request.POST.get('newpassword'))==(request.POST.get('confirmpassword')):
                user.password=request.POST.get('confirmpassword')
                user.save()
                return render(request,'Userboutique/Changepassword.html',{'err':3})
            else:
                return render(request,'Userboutique/Changepassword.html',{'err':1})
        else:
            return render(request,'Userboutique/Changepassword.html',{'err':2})
    else:
        return render(request,'Userboutique/Changepassword.html',{'i':user})

def logout(request):
    if request.method=="POST":
        logouts(request)
        return redirect('Userboutique:Userboutique')