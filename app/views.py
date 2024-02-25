from django.shortcuts import render
from .modelForm import EmployeeModelForm
from .models import Employee
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    emps = Employee.objects.all().order_by('id')
    
    paginator = Paginator(emps, 4)
    print(paginator)

    page_number = request.GET.get('page')
    print(page_number)

    page_obj = paginator.get_page(page_number)
    print(page_obj)

    total_page = paginator.num_pages
    print(total_page)

    return render(request,'home.html', context={'page_obj':page_obj,'total_page':total_page})




def create(request):
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added')
            return HttpResponseRedirect('/')
        

    form = EmployeeModelForm()
    return render(request, 'create.html',context={'form':form})


def update(request, id):
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            salary = form.cleaned_data['salary']
            date = form.cleaned_data['joining_date']

            emp = Employee(pk=id,first_name = firstName, last_name=lastName, email=email, salary=salary, joining_date=date)
            emp.save()

            messages.success(request,'Successfully Updated')
            return HttpResponseRedirect('/')

    object = Employee.objects.get(pk=id)
    form = EmployeeModelForm(instance=object)
    return render(request,'update.html',context={'form':form})


def delete(request,id):
    object = Employee.objects.get(pk=id)
    object.delete()
    messages.success(request,'Successfully Deleted')
    return HttpResponseRedirect('/')