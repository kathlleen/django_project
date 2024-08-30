from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from goods.models import Products

def index(request):

    # categories = Categories.objects.all()
    goods = Products.objects.all()[:12]

    context = {
        "title" : "SQ R3",
        # 'categories' : categories,
        "goods" : goods
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title" : "SQ R3 - About",
        "page_title" : "About",
        "page_description" : "Find out some information about us"
    }
    return render(request, 'main/about.html', context)