from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from order.models import Order, OrderItem
from shop.models import Product


@login_required
def add_to_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    order, created = Order.objects.get_or_create(user=request.user, status=False)

    order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)

    if item_created:
        order_item.number_of_sale = 1
    else:
        order_item.number_of_sale += 1

    order_item.save()

    return redirect('/shop/products/')


@login_required
def view_order(request):
    order = Order.objects.filter(user=request.user, status=False).first()

    total_price = 0
    if order:
        for item in order.orders_item.all():
            total_price += item.number_of_sale * item.product.price

    return render(request, "order/view_order.html", {"order": order, "total_price": total_price})


@login_required
def complete_order(request):
    order = Order.objects.filter(user=request.user, status=False).first()

    if order:
        order.status = True
        order.save()

    return redirect('/shop/products/')
