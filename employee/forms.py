from django import forms  
from employee.models import Employee  ,Image,GeeksModel
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'img','id')

class GeeksForm(forms.ModelForm):  
    class Meta:  
        model =  GeeksModel
        fields = "__all__" 