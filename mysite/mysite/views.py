from django.shortcuts import render




# Create your views here.

def html_home(request):
    return render(request,'home.html')

def html_contact(request):
    return render(request,'contact.html')

def html_projects(request):
    return render(request,'projects.html')
