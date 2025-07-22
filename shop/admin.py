from django.contrib import admin
from shop.models import Popular_product, Category, Discounted_product,Smartfon

# Category modeliga maxsus admin konfiguratsiya
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')  # Admin panelda ushbu ustunlar ko‘rsatiladi

# Modellarni admin panelga qo‘shish
admin.site.register(Popular_product)
admin.site.register(Category, CategoryAdmin)  # Category model maxsus konfiguratsiya bilan
admin.site.register(Discounted_product)
admin.site.register(Smartfon)
