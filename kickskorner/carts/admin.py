from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class cart_admin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

admin.site.register(Cart, cart_admin)
admin.site.register(CartItem)


