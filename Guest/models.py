from django.db import models

# Create your models here.
class tbl_user(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    phone=models.CharField(max_length=35)
    email=models.CharField(max_length=40)
    gender=models.CharField(max_length=25)
    password=models.CharField(max_length=35)
    image=models.FileField(upload_to="Userpic/")