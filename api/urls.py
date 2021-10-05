from django.urls import path
from  . import views


urlpatterns = [
    path('StudentApi/',views.StudentApi.as_view()),
    path('StudentApi/<int:pk>',views.StudentApiRDU.as_view()),
]