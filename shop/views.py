from django.shortcuts import render, get_object_or_404
from shop.models import Product, Category


def list_product(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})


def detail_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)
    if related_products.count() > 3:
        related_products = related_products.order_by('?')[:3]
    else:
        related_products = related_products[:3]

    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'shop/detail.html', context)


def list_product_for_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'shop/show_category.html', {'products': products, 'category': category})
