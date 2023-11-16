from django.db import models
from Guest.models import*
# Create your models here.
class tbl_staffreg(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    phone=models.CharField(max_length=45)
    email=models.CharField(max_length=40)
    gender=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    doj=models.DateField(auto_now_add=True,null=True)
    image=models.FileField(upload_to="Shoppic/")
    photo=models.FileField(upload_to="Shoppic/")

class tbl_admin(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=30)
    phone=models.CharField(max_length=35)
    email=models.CharField(max_length=30)
    gender=models.CharField(max_length=45)
    password=models.CharField(max_length=30)
    
class tbl_typesofservices(models.Model):
    servicestypes=models.CharField(max_length=40)

class tbl_addservices(models.Model):
    servicesdetail=models.CharField(max_length=40)
    rate=models.CharField(max_length=35)
    image=models.FileField(upload_to="Hairstylepic/")
    servicestypes=models.ForeignKey(tbl_typesofservices,on_delete=models.CASCADE) 

class tbl_workgalary(models.Model):
    workdate=models.DateField(auto_now_add=True)
    caption=models.CharField(max_length=40)
    image=models.FileField(upload_to="Workpic/")

class tbl_assignstaff(models.Model):
    staff=models.ForeignKey(tbl_staffreg,on_delete=models.CASCADE)
    booking=models.ForeignKey('Userboutique.tbl_bookingservice',on_delete=models.CASCADE)
    assign_status=models.IntegerField(default='0')
