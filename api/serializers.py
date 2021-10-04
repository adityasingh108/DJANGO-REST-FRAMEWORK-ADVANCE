import re
from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import serializers
from .models import Student


# # VALIDATIORS 
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise ValidationError('Name must be star with R')
#     return value
# class Studentserializers(serializers.Serializer):
#     name = serializers.CharField(max_length=50 ,validators=[start_with_r])
#     city = serializers.CharField(max_length=100)
#     RollNo = serializers.IntegerField()
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.city = validated_data.get('city', instance.city)
#         instance.RollNo = validated_data.get('RollNo', instance.RollNo)
#         instance.save()
#         return instance
    
    
    
#     ############### FIELD LEVEL VALIDATION ############

#     def validate_RollNo(self,value):
#         '''# FIELD LEVEL VALIDATION '''
#         if value >=100:
#             raise serializers.ValidationError('seat Full')
#         return value    


#     ################ OBJECT LEVEL VALIDATION ######
#     def validate(self,data):
#         name = data.get('name')        
#         city = data.get('city') 
#         if name.lower() == 'rohit' and city.lower() != "ranchi":
#             raise serializers.ValidationError("city must be ranchi ")
#         return data       


class Studentserializers(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)  # 3 rd way
    class Meta:
        model = Student
        fields = ['name','RollNo','city',]
        # read_only_fields = ['name','RollNo']    # 1 st way
        # extra_kwargs = {'name':{'read_only':True}}    # 2nd way
        
        