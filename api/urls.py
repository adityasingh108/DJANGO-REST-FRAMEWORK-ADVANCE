from django.urls import path
from  . import views


urlpatterns = [
    path('StudentApi/',views.StudentApiRetriveCreate.as_view()),
    path('StudentApi/<int:pk>',views.StudentApiRetriveUpdateDestroy.as_view()),
]