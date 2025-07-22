from django.urls import path
from shop.views import HomeView,categories_view,Smartfons_view,Basket_view

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('kategoriyalar/',categories_view,name='categories'),
    path('smartfonlar/',Smartfons_view,name='smartfons'),
    path('savat/',Basket_view,name='basket')
]
