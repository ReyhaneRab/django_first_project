from django.http import Http404
from django.shortcuts import render, get_object_or_404
from shop.models import Product


def list_product(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})


def detail_product(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'shop/detail.html', {'product': product})
    return Http404


def list_product_for_category(request, category_id):
    if request.method == 'GET':
        products = get_object_or_404(Product, category=category_id)
        return render(request, 'shop/show_category.html', {'products': products})
    return Http404
