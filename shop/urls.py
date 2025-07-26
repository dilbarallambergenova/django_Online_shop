from django.urls import path
from shop.views import HomeView,categories_view,category_products_view,add_to_favorites,favorite_products,toggle_favorite

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('kategoriyalar/',categories_view,name='categories'),
    path('kategoriyalar/<str:name>/',category_products_view,name='category_product'),
    path('favorites/add/<int:product_id>/',add_to_favorites,name='add_to_favorites'),
    path('favorites/',favorite_products,name='favorite_products'),
    path('favorites/toggle/<int:product_id>/', toggle_favorite, name='toggle_favorite'),

    
    # path('smartfonlar/',Smartfons_view,name='smartfons'),
    # path('savat/',Basket_view,name='basket'),
    # path('buyurtmalar/',Checkout_view,name='checkout')
]
