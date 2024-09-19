from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from order.models import Order, OrderItem
from shop.models import Product


@login_required
def add_to_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # بررسی وجود سفارش ناتمام برای کاربر
    order, created = Order.objects.get_or_create(user=request.user, status=False)

    # بررسی وجود محصول در آیتم‌های سفارش
    order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)

    # اگر محصول جدید باشد، آن را به سفارش اضافه می‌کنیم و اگر وجود داشت تعداد آن را افزایش می‌دهیم
    if not item_created:
        order_item.number_of_sale += 1
        order_item.save()
    else:
        order_item.number_of_sale = 1
        order_item.save()

    return redirect('/shop/products/')  # هدایت کاربر به صفحه لیست محصولات

# ویو مشاهده سفارش‌های کاربر
@login_required
def view_order(request):
    # گرفتن سفارش ناتمام کاربر
    order = Order.objects.filter(user=request.user, status=False).first()

    return render(request, "order/view_order.html", {"order": order})

# ویو تکمیل سفارش
@login_required
def complete_order(request):
    # پیدا کردن سفارش ناتمام کاربر
    order = Order.objects.filter(user=request.user, status=False).first()

    if order:
        order.status = True  # تغییر وضعیت سفارش به تکمیل شده
        order.save()

    return redirect('/accounts/profile/')  # هدایت به صفحه پروفایل یا هر صفحه دیگر
