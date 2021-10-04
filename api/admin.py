from django.contrib import admin
from django.db import models
from . models import Student
# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ['id','RollNo','name','city',]
admin.site.register(Student ,AdminStudent)

