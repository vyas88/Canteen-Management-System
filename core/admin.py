from django.contrib import admin
from django.contrib import admin
from core.models import CartOrderProducts, Product, Category, CartOrder, wishlist_model

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_editable = ['title', 'price', 'featured', 'deal']
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'featured','pid', 'deal']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ['paid_status','sku']
    list_display = ['user',  'price', 'paid_status', 'order_date', 'sku']

class CartOrderProductsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image','qty', 'price', 'total']

class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderProducts, CartOrderProductsAdmin)
admin.site.register(wishlist_model, wishlistAdmin)
