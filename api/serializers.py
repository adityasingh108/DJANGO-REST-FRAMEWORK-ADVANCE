import re
from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import serializers
from .models import Student




class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','rollno','city',]

        
        