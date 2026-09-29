from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "category",
        "product_type",
        "price",
        "stock",
        "active",
        "is_offer",
    )

    list_filter = (
        "category",
        "product_type",
        "active",
        "is_offer",
    )

    search_fields = (
        "name",
        "description",
    )

    @admin.display(description="Nombre")
    def product_name(self, obj):
        return f"{obj.name} ({obj.id})"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
    )

    list_filter = (
        "parent",
    )

    search_fields = (
        "name",
    )