from django.shortcuts import render
from .modelForm import EmployeeModelForm
from .models import Employee
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    emps = Employee.objects.all()
    return render(request,'home.html', context={'emps':emps})


def create(request):
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            salary = form.cleaned_data['salary']
            date = form.cleaned_data['joining_date']

            emp = Employee(first_name = firstName, last_name=lastName, email=email, salary=salary, joining_date=date)
            emp.save()

            return HttpResponseRedirect('/')

    form = EmployeeModelForm()
    return render(request, 'create.html',context={'form':form})


def update(request):
    pass


def delete(request,id):
    object = Employee.objects.get(pk=id)
    object.delete()
    return HttpResponseRedirect('/')