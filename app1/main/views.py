from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from goods.models import Products

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] =  "SQ R3"
        context['goods'] = Products.objects.all()[:12]
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SQ R3 - About"
        context["page_title"] = "About"
        context["page_description"] = "Find out some information about us"
        return context


# def index(request):
#
#     # categories = Categories.objects.all()
#     goods = Products.objects.all()[:12]
#
#     context = {
#         "title" : "SQ R3",
#         "goods" : goods
#     }
#     return render(request, 'main/index.html', context)

# def about(request):
#     context = {
#         "title" : "SQ R3 - About",
#         "page_title" : "About",
#         "page_description" : "Find out some information about us"
#     }
#     return render(request, 'main/about.html', context)