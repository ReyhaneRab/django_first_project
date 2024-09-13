from shop.models import Category


def menu_categories(request):
    categories = Category.objects.filter(show_in_menu=True).order_by('title')
    return {'menu_categories': categories}
