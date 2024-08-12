from django.shortcuts import render

def catalog(request):

    context = {
        "title" : "SQ R3 - Catalog",
        "page_title" : "Catalog",
        "page_description" : "Find out some information about us"
    }
    return render(request, 'goods/catalog.html', context)

def product(request):

    context = {
        "title" : "SQ R3 - Product name",
        "page_title" : "Product name",
        "page_description" : "Find out some information about us"
    }
    return render(request, 'goods/product.html', context)
