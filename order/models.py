from django.db import models
from core.models import CustomUser
from shop.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order_item')
    number_of_sale = models.IntegerField()

    def __str__(self):
        return self.product.title


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_order')
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='orders_item')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'


