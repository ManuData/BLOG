from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import pandas as pd
import numpy as np
import json

test_datos = [0,1,2,30,34,21]
serie = pd.Series(test_datos,name="test")
obj = {'test1':1,'test2':2}

# funciones de prueba de artículos: 

# Create your views here.
def html_article_0(request):
    return render(request,'blog/articles_0.html')

def html_article_1(request):
    return render(request,'blog/articles_1.html')


# función para todo el listado de artículos que se encuentren en la base de datos: 

def html_article_list(request):
    articles = Article.objects.all()
    response = render(request,'blog/article_list.html',{'articles':articles,'numbers':serie,"obj_as_json":json.dumps(obj)})  
    response.set_cookie('TEST', 'PUTO AMO !!')
    return response
     
# Función para la lista de artículos sin meter cookies.
#def html_article_list(request):
    #articles = Article.objects.all()
    #return render(request,'blog/article_list.html',{'articles':articles,'numbers':serie,"obj_as_json":json.dumps(obj)}) 

