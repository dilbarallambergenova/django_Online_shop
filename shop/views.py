from django.shortcuts import render,get_list_or_404,redirect
from shop.models import Popular_product,Category,Discounted_product,Smartfon
from django.views.generic import ListView,DeleteView,TemplateView
from django.http import JsonResponse
import json
# class NewsListView(ListView):
#     queryset=Shop.objects.all()
#     template_name='index.html'
#     context_object_name='products'

class HomeView(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        popular_products=Popular_product.objects.all()
        categories=Category.objects.all()
        discounted_products=Discounted_product.objects.all()
        context['popular_products']=popular_products
        context['categories']=categories
        context['dicounted_productss']=discounted_products
        return context

    

    

def categories_view(request):
    categories=Category.objects.prefetch_related('children__children').filter(parent__isnull=True)
    context={
        'categories':categories,
        'request':request
    }
    return render(request,'categories.html',context=context)

def Smartfons_view(request):
    smartfons=Smartfon.objects.all()
    context={
        'smartfons':smartfons
    }
    return render(request,'Smartfons.html',context=context)

def Basket_view(request):
    items=Popular_product.objects.all()
    context={
        'items':items
    }
    return render(request,'Basket.html',context=context)

def Checkout_view(request):
    return render(request,'checkout.html')
