from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order_item')
    number_of_sale = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_item')

    def __str__(self):
        return self.product.title

