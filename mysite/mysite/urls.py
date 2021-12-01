"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


# El parámetro "name" dentro de la función path sirve para importar las url dentro del html con la siguiente
# sintaxis: "{% url 'contact' %}"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.html_home, name='home'),
    path('projects/', views.html_projects,name = 'projects'),
    path('projects/bmind', views.html_project_bmind,name = 'project_bmind'),
    path('contact/', views.html_contact, name='contact'),
    #url(r'^test/',include('blog.urls'))
    path('blog/',include('blog.urls')),
    #path('home/',include('blog.urls')),

]
