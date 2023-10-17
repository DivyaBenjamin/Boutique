from django.db import models

# Create your models here.
class tbl_user(models.Model):
    name=models.CharField(max_length=45)
    username=models.CharField(max_length=40)
    email=models.CharField(max_length=35)
    phone=models.CharField(max_length=30)
    password=models.CharField(max_length=25)
    gender=models.CharField(max_length=20)

class tbl_staff(models.Model):
    name=models.CharField(max_length=35)
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=25)
    password=models.CharField(max_length=30)
    gender=models.CharField(max_length=20)
    dateoj=models.DateField(auto_now_add=True,null=True)

class tbl_styles(models.Model):
    styles=models.CharField(max_length=35)

class tbl_typesof(models.Model):
    typesof=models.CharField(max_length=35)
    styles=models.ForeignKey(tbl_styles,on_delete=models.CASCADE)