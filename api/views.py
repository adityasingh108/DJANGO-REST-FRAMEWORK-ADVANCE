from api.models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView



class StudentApiRetriveCreate(ListCreateAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializers
    
class StudentApiRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializers
        
 



# class StudentApi(ListModelMixin,CreateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
    
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request ,*args, **kwargs) 
    
# class StudentApiRDU(RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
    # serializer_class = StudentSerializers
    
    # def get(self,request,*args, **kwargs):
    #     return self.retrieve(request,*args, **kwargs) 
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs) 
    
    # def put(self,request,*args, **kwargs):
    #     return self.update(request,*args,**kwargs) 
    
    



# class StudentApi(APIView):
#     def get(self,request, pk=None, format=None):
#             id = pk
#             try:
#                 if id is not None:
#                     stu = Student.objects.get(id =id)
#                     serializer =StudentSerializers(stu)
#                     return Response(serializer.data)        
#                 stu = Student.objects.all()
#                 serializer = StudentSerializers(stu,many = True)
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             except:
#                 return Response({'alert':'ID does not exist. please check you input and try again.'},status=status.HTTP_404_NOT_FOUND)
   
#     def post(self, request ,pk=None, format=None):
#         serializer = StudentSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Success':'Data has been added'} ,status=status.HTTP_201_CREATED)
#         return Response({'alert':serializer.errors} ,status=status.HTTP_400_BAD_REQUEST)        
                
#     def put(self,request ,pk=None,format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Success':'Data has been updated'},status=status.HTTP_202_ACCEPTED)
#         return Response({'Alert':serializer.errors} ,status=status.HTTP_400_BAD_REQUEST)
          
                 
#     def patch(self, request ,pk=None ,format=None):
#         stu= Student.objects.get(pk=pk)
#         serializer = StudentSerializers(stu ,data=request.data ,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Success':'Data has been updated'},status=status.HTTP_206_PARTIAL_CONTENT)
#         return Response({'Alert':serializer.errors} ,status=status.HTTP_400_BAD_REQUEST)    

#     def delete(self,request,pk=None,format=None):
#         id =pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'Success':'Data has been deleted'}) 