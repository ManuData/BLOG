from django.shortcuts import render
import datetime




# Create your views here.

def html_home(request):
    return render(request,'home.html')

def html_contact(request):
    return render(request,'contact.html')

def html_projects(request):
    fecha_actual = datetime.datetime.now()
    return render(request,'projects.html',{'fecha_actual':fecha_actual})


def html_project_bmind(request):
    return render(request,'project_bmind.html')

