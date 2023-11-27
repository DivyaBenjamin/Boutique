from rest_framework import serializers
from .models import tbl_typesofservices

class typeserviceserializer(serializers.ModelSerializer):
    class Meta:
        model=tbl_typesofservices
        fields=['id','servicestypes']