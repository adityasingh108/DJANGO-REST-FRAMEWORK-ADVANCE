from django.urls import path
from  . import views


urlpatterns = [
    # path('studentInfo/<int:id>/',views.studentInfo_id,name='studentInfo_id'),
    # path('studentInfo/',views.studentInfo,name='studentInfo'),
    # path('CreateStudentInfo/',views.CreateStudentInfo,name='CreateStudentInfo'),
    # path('StudentApi/',views.StudentApi ,name="StudentApi"),   BY FUNCTION BASED
    path('StudentApi/',views.StudentApi.as_view()),
]