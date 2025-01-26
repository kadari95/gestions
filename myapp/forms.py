from django.core import  validators
from django import forms
from .models import Student

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','adresse','sexe','age']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse' : forms.TextInput(attrs={'class':'form-control'}),
            'sexe' : forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
        }