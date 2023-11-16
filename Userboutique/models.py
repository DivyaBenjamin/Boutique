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