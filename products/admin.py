from django.contrib import admin
from .models import Product, Room


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
    )

    ordering = ('sku',)


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Room, RoomAdmin)
