from .models import Employee
from django.forms import ModelForm

class EmployeeModelForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','email','salary','joining_date']