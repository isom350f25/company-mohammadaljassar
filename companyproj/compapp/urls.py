from django.urls import path
from . import views

urlpatterns = [
    path('employees_list/', views.employee_view, name='employee_list'),
]