from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def html_home(request):
    return render(request,'home_minimal.html')

def html_contact(request):
    return render(request,'contact.html')

def html_projects(request):
    return render(request,'projects.html')
