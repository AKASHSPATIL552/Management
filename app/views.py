from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages

# Create your views here.

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee {form.instance.first_name} {form.instance.last_name} details added successfully!')
            return redirect('list_employees')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'list_employees.html', {'employees': employees})

def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee {employee.first_name} {employee.last_name} details updated successfully!')
            return redirect('list_employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    messages.success(request, f'Employee {employee.first_name} {employee.last_name} details deleted successfully!')
    return redirect('list_employees')

