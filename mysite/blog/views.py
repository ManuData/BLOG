from django.shortcuts import render


# Create your views here.
def html_test(request):
    return render(request,'blog/articles.html')

