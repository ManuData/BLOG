from django.db import models
from django.db.models.fields import DateField, SlugField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    # Es la dirección del artículo
    slug = models.SlugField()
    body = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now_add = True)

    

    # Add in thumbnail later
    # Add in author later







