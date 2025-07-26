from django.shortcuts import render,get_object_or_404,redirect
from shop.models import Category,Product
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
        popular_products=Product.objects.filter(is_popular=True)
        discounted_products=Product.objects.filter(discount_price__isnull=False)
        categories=Category.objects.all()
        context['popular_products']=popular_products
        context['discounted_products']=discounted_products
        context['categories']=categories
        context['favorites'] = self.request.session.get('favorites', [])

        return context

    

    

def categories_view(request):
    categories=Category.objects.prefetch_related('children__children').filter(parent__isnull=True)
    context={
        'categories':categories,
        'request':request
    }
    return render(request,'categories.html',context=context)

def category_products_view(request,name):
    category=get_object_or_404(Category,name=name)
    products=Product.objects.filter(category=category)
    context={
        'category':category,
        'products':products
    }
    return render(request,'category_product.html',context)
# def Smartfons_view(request):
#     smartfons=Smartfon.objects.all()
def add_to_favorites(request, product_id):
    # product = get_object_or_404(Product, id=product_id)
    favorites = request.session.get('favorites', [])
    if product_id not in favorites:
        favorites.append(product_id)
        request.session['favorites'] = favorites
        request.session.modified = True  # bu muhim!

    return JsonResponse({'success': True})

def favorite_products(request):
    favorites = request.session.get('favorites', [])
    products = Product.objects.filter(id__in=favorites)
    return render(request, 'favorite.html', {'products': products})

def toggle_favorite(request, product_id):
    favorites = request.session.get('favorites', [])

    if product_id in favorites:
        favorites.remove(product_id)
        action = 'removed'
    else:
        favorites.append(product_id)
        action = 'added'

    request.session['favorites'] = favorites
    request.session.modified = True

    return JsonResponse({'success': True, 'action': action})
