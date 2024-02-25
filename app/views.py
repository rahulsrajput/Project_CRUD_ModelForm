from django.shortcuts import render

from .models import Employee
# Create your views here.
def home(request):
    emps = Employee.objects.all()
    return render(request,'home.html', context={'emps':emps})


def create(request):
    pass


def update(request):
    pass


def delete(request):
    pass