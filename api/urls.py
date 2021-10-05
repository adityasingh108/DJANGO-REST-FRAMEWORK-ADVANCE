from django.urls import path
from  . import views


urlpatterns = [
    path('StudentApi/',views.StudentApi),
    path('StudentApi/<int:pk>',views.StudentApi),
]