from django.contrib import admin
from .models import *

# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ('name','adresse','sexe','age')



admin.site.register(Student, AdminStudent)
