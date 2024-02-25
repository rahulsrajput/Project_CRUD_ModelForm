from .models import Employee
from django.forms import ModelForm
from django import forms

class EmployeeModelForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','email','salary','joining_date']

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'salary':forms.NumberInput(attrs={'class':'form-control'}),
            'joining_date':forms.DateInput(attrs={'class':'form-control'})
        }