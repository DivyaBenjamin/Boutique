from django.db import models
from Guest.models import*
from Admin.models import*
# Create your models here.
class tbl_bookingservice(models.Model):
    booking_status=models.CharField(max_length=1,default='0')
    booking_date=models.DateField(auto_now_add=True,null=True)
    booked_date=models.DateField(null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    services=models.ForeignKey(tbl_addservices,on_delete=models.CASCADE,null=True)

class tbl_blogs(models.Model):
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=40)
    blog_date=models.DateField(auto_now_add=True,null=True)

class tbl_feedback(models.Model):
    message=models.CharField(max_length=40)
    message_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.SET_NULL,null=True)
    staff=models.ForeignKey(tbl_staffreg,on_delete=models.SET_NULL,null=True)

class tbl_contactus(models.Model):
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=35)
    email=models.CharField(max_length=33)
    message=models.CharField(max_length=30)
    date=models.DateField(auto_now_add=True,null=True)