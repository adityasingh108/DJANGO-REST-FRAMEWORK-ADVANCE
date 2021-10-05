from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import Student
from .serializers import StudentSerializers
from api import serializers


class StudentApi(APIView):
    def get(self,request, pk=None, format=None):
            id = pk
            try:
                if id is not None:
                    stu = Student.objects.get(id =id)
                    serializer =StudentSerializers(stu)
                    return Response(serializer.data)        
                stu = Student.objects.all()
                serializer = StudentSerializers(stu,many = True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                return Response({'alert':'ID does not exist. please check you input and try again.'},status=status.HTTP_404_NOT_FOUND)
   
    def post(self, request ,pk=None, format=None):
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success':'Data has been added'} ,status=status.HTTP_201_CREATED)
        return Response({'alert':serializer.errors} ,status=status.HTTP_400_BAD_REQUEST)        
                
    def put(self,request ,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success':'Data has been updated'},status=status.HTTP_202_ACCEPTED)
        return Response({'Alert':serializer.errors} ,status=status.HTTP_400_BAD_REQUEST)
          
                 
    def patch(self, request ,pk=None ,format=None):
        stu= Student.objects.get(pk=pk)
        serializer = StudentSerializers(stu ,data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success':'Data has been updated'},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({'Alert':serializer.errors} ,status=status.HTTP_400_BAD_REQUEST)    

    def delete(self,request,pk=None,format=None):
        id =pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'Success':'Data has been deleted'}) 