from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        "title" : "SQ R3"
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title" : "SQ R3 - About",
        "page_title" : "About",
        "page_description" : "Find out some information about us"
    }
    return render(request, 'main/about.html', context)