from rest_framework import serializers
from .models import tbl_blogs

class blogserializer(serializers.ModelSerializer):
    class Meta:
        model=tbl_blogs
        fields=['id','subject','message']