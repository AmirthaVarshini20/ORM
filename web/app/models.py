from django.db import models
from django.contrib import admin
class Employee(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    experience=models.IntegerField()


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','name','salary','age')