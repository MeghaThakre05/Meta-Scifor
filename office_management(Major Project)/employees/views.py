# employees/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from .forms import EmployeeSearchForm

def home(request):
    return render(request, 'home.html')

def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'view_employees.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_employees')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

# Update Employee
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form, 'employee': employee})

# Delete Employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('view_employees')
    return render(request, 'delete_employee.html', {'employee': employee})

# Search Employee
def employee_search(request):
    form = EmployeeSearchForm(request.GET)
    employees = Employee.objects.all()  # Start with all employees

    if form.is_valid():
        # Filter employees based on form fields
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        department = form.cleaned_data.get('department')
        position = form.cleaned_data.get('position')

        if first_name:
            employees = employees.filter(first_name__icontains=first_name)
        if last_name:
            employees = employees.filter(last_name__icontains=last_name)
        if department:
            employees = employees.filter(department__icontains=department)
        if position:
            employees = employees.filter(position__icontains=position)

    return render(request, 'search_results.html', {
        'form': form,
        'employees': employees
    })

