from django.shortcuts import render
from goods.models import Categories, Products
def catalog(request):
    categories = Categories.objects.all()
    goods = Products.objects.all()

    context = {
        "title" : "SQ R3 - Catalog",
        "page_title" : "Catalog",
        "page_description" : "Find out some information about us",
        'categories': categories,
        'goods' : goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request):

    context = {
        "title" : "SQ R3 - Product name",
        "page_title" : "Product name",
        "page_description" : "Find out some information about us"
    }
    return render(request, 'goods/product.html', context)
