from audioop import reverse
from multiprocessing import context
from django.shortcuts import redirect, render

from register.models import Employee
from .forms import EmployeeForm
from django.urls import reverse
from .models import Employee

def employe_list(request):
    context ={'employees': Employee.objects.all()}
    return render(request, "register/employee_list.html", context)
    
    #return render(request, "register/employee_list.html" , 'employees' :employee.objects.all()}
    

def employe_form(request, id=0):
    if request.method == "POST":  
        if id ==0 : #means its an insert operation
            form = EmployeeForm(request.POST) 
        else: #Update operation
            employee = Employee.objects.get(pk = id) 
            form = EmployeeForm(request.POST, instance = employee) 
        if form.is_valid():
            form.save()
        return redirect(reverse('list'))    
    else : 
        if id ==0 :  #Edit operation
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)   
            form = EmployeeForm(instance = employee) 
        return render(request, "register/employee_form.html", {'form':form})

def employe_delete(request, id):
    employee = Employee.objects.get(pk = id) 
    employee.delete()
    return redirect(reverse('list'))


