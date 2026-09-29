from django.contrib import admin
from .models import Address, Order, OrderItem


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "user",
        "city",
        "region",
    )

    search_fields = (
        "full_name",
        "user__username",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "total_amount",
        "is_paid",
        "created_at",
    )

    list_filter = (
        "is_paid",
        "created_at",
    )

    search_fields = (
        "user__username",
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
        "total_price",
    )

    search_fields = (
        "product__name",
        "order__user__username",
    )