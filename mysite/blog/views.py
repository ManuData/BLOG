from django.shortcuts import render
from .models import Article

# funciones de prueba de artículos: 

# Create your views here.
def html_article_0(request):
    return render(request,'blog/articles_0.html')

def html_article_1(request):
    return render(request,'blog/articles_1.html')


# función para todo el listado de artículos que se encuentren en la base de datos: 

def html_article_list(request):
    articles = Article.objects.all()
    return render(request,'blog/article_list.html',{'articles':articles})   