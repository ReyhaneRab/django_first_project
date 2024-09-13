def link_creator(request, path):
    return "#" if request.path == path else path


def menu_context_processor(request):
    return {
        "menu": [
            dict(title="Home", link=link_creator(request, "/shop/products/")),
            dict(title="About", link=link_creator(request, "...")),
            dict(title="Products", link=link_creator(request, "/shop/products/")),
        ]
    }
