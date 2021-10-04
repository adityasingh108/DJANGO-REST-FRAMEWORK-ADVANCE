from functools import partial
from django import http
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.utils import json
from . models import Student
from .serializers import Studentserializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io


# Create your views here.

# def studentInfo_id(request ,id):
#     # FOR MODEL OBJECT  use get and id and for for query set use many = True
#     stu = Student.objects.get(id=id)
#     serialzer  = Studentserializers(stu)
#     # METHOD === 1
    
#     # json_data = JSONRenderer().render(serialzer.data)
#     # return HttpResponse(json_data, content_type = 'application/json')
    
#     # METHOD == 2
#     return JsonResponse(serialzer.data,safe=False)

# def studentInfo(request):
#     # FOR MODEL OBJECT  use get and id and for for query set use many = True
#     stu = Student.objects.all()
#     serialzer  = Studentserializers(stu ,many=True)
#     # METHOD ++ 1
    
#     # json_data = JSONRenderer().render(serialzer.data)
#     # return HttpResponse(json_data, content_type = 'application/json')
    
#     # METHOD ++ 2
    
#     return JsonResponse(serialzer.data,safe=False)

# @csrf_exempt
# def CreateStudentInfo(request):
    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializers = Studentserializers(data = python_data)
#         if serializers.is_valid():
#             serializers.save()
#             res = {'Message ':'Data has been created'}
#             return JsonResponse(res)
#         else:
#             return JsonResponse(serializers.errors)
        
# @csrf_exempt
# def StudentApi(request):
#     # Get method 
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         print(python_data)
#         id = python_data.get('id' ,None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = Studentserializers(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type = 'application/json')
#         stu = Student.objects.all()
#         serializer = Studentserializers(stu ,many= True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type = 'application/json')
    
#     if request.method =="POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializers = Studentserializers(data = python_data)
#         if serializers.is_valid():
#             serializers.save()
#             res = {'Message ':'Data has been created'}
#             return JsonResponse(res)
#         else:
#             return JsonResponse(serializers.errors)
        
#     if request.method =="PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         print(id)
#         stu = Student.objects.get(id=id)
#         serializer =Studentserializers(stu, data=python_data ,partial=False)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {'message':'data has been updated'}
#             # json_data = JSONRenderer().render(msg)
#             # return HttpResponse(json_data,content_type = 'application/json')
#             return JsonResponse(msg)
        
        
#         return JsonResponse(serializer.errors)  
    
#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         print(id)
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         msg = {'message':'Data has been deleted'}
#         return JsonResponse(msg)
        
@method_decorator(csrf_exempt,name='dispatch')    
class StudentApi(View):
    def get(self,request,*args, **kwargs):
        if request.method == "GET":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            print(python_data)
            id = python_data.get('id' ,None)
            try:
                if id is not None:
                    stu = Student.objects.get(id=id)
                    serializer = Studentserializers(stu)
                    json_data = JSONRenderer().render(serializer.data)
                    return HttpResponse(json_data,content_type = 'application/json')
                stu = Student.objects.all()
                serializer = Studentserializers(stu ,many= True)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data,content_type = 'application/json') 
            except:
                msg = {'alert':'it seems like data  has been deleted'}
                return JsonResponse(msg)
        
        
    def post(self,request,*args, **kwargs):
        if request.method =="POST":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializers = Studentserializers(data = python_data ,partial=True)
            if serializers.is_valid():
                serializers.save()
                res = {'Message ':'Data has been created'}
                return JsonResponse(res)
            else:
                return JsonResponse(serializers.errors)
    def put(self,request,*args, **kwargs):
        if request.method =="PUT":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            print(id)
            stu = Student.objects.get(id=id)
            serializer =Studentserializers(stu, data=python_data ,partial=True)
            if serializer.is_valid():
                serializer.save()
                msg = {'message':'data has been updated'}
                # json_data = JSONRenderer().render(msg)
                # return HttpResponse(json_data,content_type = 'application/json')
                return JsonResponse(msg)
            
    def delete(self,request,*args, **kwargs):
        if request.method == "DELETE":
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            print(id)
            stu = Student.objects.get(id=id)
            stu.delete()
            msg = {'message':'Data has been deleted'}
            return JsonResponse(msg)
                
                
                    
