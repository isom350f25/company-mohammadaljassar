from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'position', 'phone_number', 'joined_on')
    search_fields = ('name', 'position')
    list_filter = ('joined_on',)
    pass