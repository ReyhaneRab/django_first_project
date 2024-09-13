from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('username',)
    search_fields = ('username',)
    search_help_text = "Search based on the username of the user ..."


admin.site.register(CustomUser, CustomUserAdmin)
