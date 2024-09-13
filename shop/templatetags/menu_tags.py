from django import template
from shop.models import Category

register = template.Library()


@register.simple_tag
def get_menu_categories():
    return Category.objects.filter(show_in_menu=True).order_by('title')
