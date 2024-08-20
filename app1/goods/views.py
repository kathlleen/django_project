from django.shortcuts import render
from goods.models import Products
def catalog(request, category_slug):
    # categories = Categories.objects.all()

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Raginator()

    context = {
        "title" : "SQ R3 - Catalog",
        "page_title" : "Catalog",
        "page_description" : "Order best furniture right now",
        # 'categories': categories,
        'goods' : goods,
    }

    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product_val = Products.objects.get(slug=product_slug)
    context = {
        'product':product_val
    }
    return render(request, 'goods/product.html', context=context)

# def product(request):
#
#     context = {
#         "title" : "SQ R3 - Product name",
#         "page_title" : "Product name",
#         "page_description" : "Find out some information about us"
#     }
#     return render(request, 'goods/product.html', context)
