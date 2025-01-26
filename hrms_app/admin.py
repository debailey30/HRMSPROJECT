# filepath: /c:/Users/DeeAnn/Desktop/HRMSPROJECT/hrms_app/admin.py
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_hired')

admin.site.register(Employee, EmployeeAdmin)
