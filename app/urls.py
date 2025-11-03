from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_employee, name='add_employee'),
    path('list/', views.list_employees, name='list_employees'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]
