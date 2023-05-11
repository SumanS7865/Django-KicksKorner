from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'selling_price', 'discounted_price','category', 'created_date','modified_date', 'is_available')
    


admin.site.register(Product,ProductAdmin)

