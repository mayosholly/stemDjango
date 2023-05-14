from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
# Create your views here.

def home(request):
    persons = Person.objects.all()
    return render(request, 'crud/index.html', {
        'persons' : persons
    })

def create(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        person = Person()
        person.firstname = firstname        
        person.lastname = lastname        
        person.phonenumber = phone        
        person.address = address   
        person.save()
        return redirect('home')
    else:     
        return render(request, 'crud/create.html')
