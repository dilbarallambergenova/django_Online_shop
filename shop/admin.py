from django.contrib import admin
from shop.models import Product,Category

# Category modeliga maxsus admin konfiguratsiya
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')  # Admin panelda ushbu ustunlar ko‘rsatiladi

# Modellarni admin panelga qo‘shish
admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)  # Category model maxsus konfiguratsiya bilan
# admin.site.register(Discounted_product)
# admin.site.register(Smartfon)
