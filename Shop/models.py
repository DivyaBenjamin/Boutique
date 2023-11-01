from django.db import models
from Admin.models import*
# Create your models here.
class tbl_addingstyles(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=30)
    image=models.FileField(upload_to="Hairstylepic/")
    typesof=models.ForeignKey(tbl_typesof,on_delete=models.CASCADE)

class tbl_addinghair(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=30)
    image=models.FileField(upload_to="Haircut/")
    haircuts=models.ForeignKey(tbl_haircuts,on_delete=models.CASCADE)
    typesofhair=models.ForeignKey(tbl_typesofhair,on_delete=models.CASCADE)

class tbl_addingcoloring(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=30)
    image=models.FileField(upload_to="Haircolor/")
    haircoloring=models.ForeignKey(tbl_haircoloring,on_delete=models.CASCADE)
    typesofhair=models.ForeignKey(tbl_typesofcoloring,on_delete=models.CASCADE)

