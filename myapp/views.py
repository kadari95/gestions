from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Student

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['adresse']
            se=fm.cleaned_data['sexe']
            ag=fm.cleaned_data['age']
            reg=Student(name=nm,adresse=em,sexe=se,age=ag)
            reg.save()
            fm =RegistrationForm()
            stud =Student.objects.all()
    else:
        fm =RegistrationForm()
        stud =Student.objects.all()
    return render(request,'index.html', {'form':fm, 'studs':stud } )


#function remove

def remove_data(request, id):

    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



def update_data(request, id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=RegistrationForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=RegistrationForm(instance=pi)

    return render(request,'update.html',{'form':fm})

