from django.shortcuts import render

def catalog(request):

    context = {
        "title" : "SQ R3 - Catalog",
        "page_title" : "Catalog",
        "page_description" : "Find out some information about us",
        "goods" : [
            {
                "title" : "Furniture name",
                "price" : "$250",
                "description" : "It is a long established fact that a reader will be the service.",
                "image" : "img/f1.jfif"
            },
            {
                "title": "Furniture name",
                "price": "$250",
                "description": "It is a long established fact that a reader will be the service.",
                "image": "img/f2.jfif"
            },
            {
                "title" : "Furniture name",
                "price" : "$250",
                "description" : "It is a long established fact that a reader will be the service.",
                "image" : "img/f3.jfif"
            },
            {
                "title" : "Furniture name",
                "price" : "$250",
                "description" : "It is a long established fact that a reader will be the service.",
                "image" : "img/f4.jfif"
            },
            {
                "title": "Furniture name",
                "price": "$250",
                "description": "It is a long established fact that a reader will be the service.",
                "image": "img/f1.jfif"
            },
            {
                "title": "Furniture name",
                "price": "$250",
                "description": "It is a long established fact that a reader will be the service.",
                "image": "img/f2.jfif"
            },
            {
                "title": "Furniture name",
                "price": "$250",
                "description": "It is a long established fact that a reader will be the service.",
                "image": "img/f3.jfif"
            },
            {
                "title": "Furniture name",
                "price": "$250",
                "description": "It is a long established fact that a reader will be the service.",
                "image": "img/f4.jfif"
            }
        ]

    }
    return render(request, 'goods/catalog.html', context)

def product(request):

    context = {
        "title" : "SQ R3 - Product name",
        "page_title" : "Product name",
        "page_description" : "Find out some information about us"
    }
    return render(request, 'goods/product.html', context)
