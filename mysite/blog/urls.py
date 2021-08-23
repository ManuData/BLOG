
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$',views.html_test),
    path('article_0',views.html_article_0),
    path('article_1',views.html_article_1),
]
