from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'cover_image', 'is_available')
    list_display_links = ('id', 'title')
    list_filter = ('is_available',)
    search_fields = ('title', 'isbn')
    search_help_text = "Search based on the title or isbn of the product ..."
    readonly_fields = ('is_available',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show_in_menu')
    list_display_links = ('id', 'title')
    list_filter = ('show_in_menu',)
    search_fields = ('title',)
    search_help_text = "Search based on the title of the category ..."


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
