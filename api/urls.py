from django.urls import path ,include
from  api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student',views.StudentViewset ,basename='Student')

urlpatterns = [
    # path('StudentApi/',views.StudentApiRetriveCreate.as_view()),
    # path('StudentApi/<int:pk>',views.StudentApiRetriveUpdateDestroy.as_view()),
    path('',include(router.urls))
]