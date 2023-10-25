from django.db import models
from Admin.models import*
# Create your models here.
class tbl_addingstyles(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=30)
    image=models.FileField(upload_to="Hairstylepic/")
    typesof=models.ForeignKey(tbl_typesof,on_delete=models.CASCADE)

