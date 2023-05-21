from django.contrib import admin
from .models import Product, Variation, Slider, Staff

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_name",)}
    list_display = (
        "product_name",
        "selling_price",
        "discounted_price",
        "category",
        "created_date",
        "modified_date",
        "is_available",
    )


class VariationAdmin(admin.ModelAdmin):
    list_display = ("product", "variation_category", "variation_value", "is_active")
    list_editable = ("is_active",)
    list_filter = ("product", "variation_category", "variation_value")


class StaffAdmin(admin.ModelAdmin):
    list_display = (
        "staff_name",
        "role",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Slider)
admin.site.register(Staff, StaffAdmin)
