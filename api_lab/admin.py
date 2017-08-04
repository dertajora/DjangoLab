from django.contrib import admin
from .models import Product


# detail display in admin for each model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name','product_type','description')
    exclude = ('description',)

# Register your models here.
admin.site.register(Product, ProductAdmin)

