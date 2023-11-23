from django.shortcuts import render,redirect
from Userboutique.models import *
from Guest.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def Userboutique(request):
    if 'uid' in request.session:
        User=tbl_user.objects.get(id=request.session['uid'])
        return render(request,'Userboutique/home.html',{'i':User})
    else:
        return redirect('webguest:login')


def styles(request):
    if 'uid' in request.session:
        stypedata=tbl_typesofservices.objects.all()
        userdata=tbl_user.objects.get(id=request.session["uid"])
        servicesdata=tbl_addservices.objects.all()
        return render(request,'Userboutique/Styles.html',{'servicestypes':stypedata,'services':servicesdata})
    else:
        return redirect('webguest:login')

def ajaxservice(request):
    types=tbl_typesofservices.objects.get(id=request.GET.get("sid"))
    services=tbl_addservices.objects.filter(servicestypes=types)
    return render(request,"Userboutique/Ajaxservice.html",{'services':services})

def bookingservice(request,pid):
    if 'uid' in request.session:
        bookingservicedata=tbl_bookingservice.objects.all()
        userdata=tbl_user.objects.get(id=request.session["uid"])
        serviceid=tbl_addservices.objects.get(id=pid)
        if request.method=="POST":
            tbl_bookingservice.objects.create(booked_date=request.POST.get('Bookeddate'),user=userdata,services=serviceid)
            return redirect('Userboutique:Userboutique')
        else:
            return render(request,'Userboutique/Bookingservice.html',{'err':2})
    else:
        return redirect('webguest:login')

def about(request):
    if 'uid' in request.session:
        contactdata=tbl_contactus.objects.all()
        if request.method=="POST":
            tbl_contactus.objects.create(name=request.POST.get('name'),phone=request.POST.get('phone'),email=request.POST.get('email'),message=request.POST.get('message'))
            return render(request,'Userboutique/About.html',{'err':2})
        else:
            return render(request,'Userboutique/About.html',{'data':contactdata})
    else:
        return redirect('webguest:login')

def blog(request):
    if 'uid' in request.session:
        blogdata=tbl_blogs.objects.all()
        if request.method=="POST":
            tbl_blogs.objects.create(subject=request.POST.get('subject'),message=request.POST.get('message'))
            return render(request,'Userboutique/Blog.html',{'err':2})
        else:
            return render(request,'Userboutique/Blog.html',{'data':blogdata})
    else:
        return redirect('webguest:login')

def feedback(request):
    if 'uid' in request.session:
        feedbackdata=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            tbl_feedback.objects.create(message=request.POST.get('message'),user=feedbackdata)
            return redirect('Userboutique:feedback')
        else:
            return render(request,'Userboutique/Feedback.html')
    else:
        return redirect('webguest:login')

def profile(request):
    if 'uid' in request.session:
        User=tbl_user.objects.get(id=request.session['uid'])
        return render(request,'Userboutique/Profile.html',{'i':User})
    else:
        return redirect('webguest:login')

def editprofile(request):
    if 'uid' in request.session:
        edituser=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            edituser.name=request.POST.get('name')
            edituser.username=request.POST.get('username')
            edituser.save()
            return redirect('Userboutique:editprofile')
        else:
            return render(request,'Userboutique/Editprofile.html',{'i':edituser})
    else:
        return redirect('webguest:login')

def changepassword(request):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            if (user.password)==(request.POST.get('currentpassword')):
                if (request.POST.get('newpassword'))==(request.POST.get('confirmpassword')):
                    user.password=request.POST.get('confirmpassword')
                    user.save()
                    email=user.email
                    send_mail(
                            'Respected Sir/Madam ',#subject
                            "\rYour password is changed"
                            "\r By"
                            "\r AngelSusy" ,#body
                            settings.EMAIL_HOST_USER,
                            [email],
                        )
                    return render(request,'Userboutique/Changepassword.html',{'err':3})
                else:
                    return render(request,'Userboutique/Changepassword.html',{'err':1})
            else:
                return render(request,'Userboutique/Changepassword.html',{'err':2})
        else:
            return render(request,'Userboutique/Changepassword.html',{'i':user})
    else:
        return redirect('webguest:login')

def logout(request):
    del request.session['uid']
    return redirect('webguest:login')