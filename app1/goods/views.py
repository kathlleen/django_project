from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from goods.models import Products

from django.views.generic import DetailView, ListView

from goods.utils import q_search


# from app1.goods.utils import q_search



class CatalogView(ListView):
    # model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 4

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')
        query = self.request.GET.get('q')

        if category_slug == 'all':
            goods = Products.objects.all()
        elif query:
            goods = q_search(query)
        else:
            goods = Products.objects.filter(category__slug=category_slug)
            # if not goods.exists():
            #     raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        return goods
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] =  'SQ R3 - Catalog'
        context['slug_url'] = self.kwargs.get('category_slug')
        return context


class ProductView(DetailView):

    # model = Products
    # slug_field = 'slug'
    template_name = 'goods/product.html'
    slug_url_kwarg = "product_slug"
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] =  self.object.name
        return context

# def catalog(request, category_slug=None):
#     page = int(request.GET.get('page', 1))
#     on_sale = request.GET.get('on_sale', None)
#     order_by = request.GET.get('order_by', None)
#     query = request.GET.get('q', None)
#
#     if category_slug == 'all':
#         goods = Products.objects.all()
#     elif query:
#         goods = q_search(query)
#     else:
#         goods = Products.objects.filter(category__slug=category_slug)
#
#     if on_sale:
#         goods = goods.filter(discount__gt=0)
#     if order_by and order_by != "default":
#         goods = goods.order_by(order_by)
#
#     paginator = Paginator(goods, 4)
#     current_page = paginator.page(page)
#
#     context = {
#         "title" : "SQ R3 - Catalog",
#         "page_title" : "Catalog",
#         "page_description" : "Order best furniture right now",
#         # 'categories': categories,
#         'goods' : current_page,
#         'slug_url' : category_slug
#     }
#
#     return render(request, 'goods/catalog.html', context)





# def product(request, product_slug):
#
#     product_val = Products.objects.get(slug=product_slug)
#     context = {
#         'product':product_val,
#         'title':product_val.name
#     }
#     return render(request, 'goods/product.html', context=context)

# def product(request):
#
#     context = {
#         "title" : "SQ R3 - Product name",
#         "page_title" : "Product name",
#         "page_description" : "Find out some information about us"
#     }
#     return render(request, 'goods/product.html', context)
