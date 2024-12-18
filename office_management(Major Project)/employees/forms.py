# employees/forms.py

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'department', 'position', 'date_joined']


class EmployeeSearchForm(forms.Form):
    first_name = forms.CharField(required=False, max_length=100)
    last_name = forms.CharField(required=False, max_length=100)
    department = forms.CharField(required=False, max_length=100)
    position = forms.CharField(required=False, max_length=100)