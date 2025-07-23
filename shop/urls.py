from django.urls import path
from shop.views import HomeView,categories_view,category_products_view

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('kategoriyalar/',categories_view,name='categories'),
    path('kategoriyalar/<str:name>/',category_products_view,name='category_product')
    # path('smartfonlar/',Smartfons_view,name='smartfons'),
    # path('savat/',Basket_view,name='basket'),
    # path('buyurtmalar/',Checkout_view,name='checkout')
]
