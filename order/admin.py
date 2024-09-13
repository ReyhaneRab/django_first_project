from django.contrib import admin
from .models import OrderItem, Order


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number_of_sale')
    list_filter = ('number_of_sale',)
    search_fields = ('product', )
    search_help_text = "Search based on the title of the product ..."


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_item', 'status')
    list_filter = ('status',)
    search_fields = ('user', 'order_item')
    search_help_text = "Search based on the order_item or user ..."


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
