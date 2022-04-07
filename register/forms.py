from turtle import position
from attr import field
from django import  forms
from .models import  Employee 

class EmployeeForm(forms.ModelForm):
    class Meta : 
        model = Employee
        fields= ('fullname' , 'mobile',  'position' ,'emp_code' )
        labels = {
                'fullname' : 'Full Name' ,
                'mobile' : 'Mobile',
                'position' : 'Position' ,
                'emp_code' : 'EMP Code'
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['position'].required = True