from django.shortcuts import render,redirect
from Shop.models import *
from Admin.models import *
from Userboutique.models import *

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def shopboutique(request):
    if 'sid' in request.session:
        return render(request,'Shop/Home.html')
    else:
        return redirect('webguest:login')

def profile(request):
    if 'sid' in request.session:
        Staff=tbl_staffreg.objects.get(id=request.session['sid'])
        return render(request,'Shop/Profile.html',{'i':Staff})
    else:
        return redirect('webguest:login')

def editprofile(request):
    if 'sid' in request.session:
        editstaff=tbl_staffreg.objects.get(id=request.session['sid'])
        if request.method=="POST":
            editstaff.name=request.POST.get('name')
            editstaff.username=request.POST.get('username')
            editstaff.save()
            return redirect('shopboutique:editprofile')
        else:
            return render(request,'Shop/Editprofile.html',{'i':editstaff})
    else:
        return redirect('webguest:login')

def changepassword(request):
    if 'sid' in request.session:
        staff=tbl_staffreg.objects.get(id=request.session['sid'])
        if request.method=="POST":
            if (staff.password)==(request.POST.get('currentpassword')):
                if (request.POST.get('newpassword'))==(request.POST.get('confirmpassword')):
                    staff.password=request.POST.get('confirmpassword')
                    staff.save()
                    email=staff.email
                    send_mail(
                            'Respected Sir/Madam ',#subject
                            "\rYour password is changed"
                            "\r By"
                            "\r AngelSusy" ,#body
                            settings.EMAIL_HOST_USER,
                            [email],
                        )
                    return render(request,'Shop/Changepassword.html',{'err':3})
                else:
                    return render(request,'Shop/Changepassword.html',{'err':1})
            else:
                return render(request,'Shop/Changepassword.html',{'err':2})
        else:
            return render(request,'Shop/Changepassword.html',{'i':staff})
    else:
        return redirect('webguest:login')

def viewfeedback(request):
    if 'sid' in request.session:
        user=tbl_user.objects.all()
        feedbackdata=tbl_feedback.objects.filter(user_id__in=user)
        return render(request,'Shop/Viewfeedback.html',{'feedback':feedbackdata})
    else:
        return redirect('webguest:login')

def viewassigned(request):
    if 'sid' in request.session:
        booking=tbl_bookingservice.objects.all()
        assigndata=tbl_assignstaff.objects.filter(assign_status=1)
        return render(request,'Shop/Viewassigned.html',{'assignstaff':assigndata})
    else:
        return redirect('webguest:login')

def logout(request):
    del request.session['sid']
    return redirect('webguest:login')