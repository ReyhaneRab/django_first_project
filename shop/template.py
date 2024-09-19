from shop.models import Category


def link_creator(request, path):
    return "#" if request.path == path else path


def menu_context_processor(request):
    my_list = [
        dict(title="Home", link=link_creator(request, "/shop/products/")),
        dict(title="About", link=link_creator(request, "...")),
        dict(title="Products", link=link_creator(request, "/shop/products/"))]
    for cat in Category.objects.all():
        my_list.append(dict(title=cat.title, link=link_creator(request, f"/shop/products/category/{cat.id}")))
    return {
        'menu': my_list

    }

