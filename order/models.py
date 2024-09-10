from django.db import models
from core.models import CustomUser
from shop.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name=...)
    number_of_sale = ...

    def __str__(self):
        return self.product


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name=...)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name=...)
    status = ...
    created_at = ...
    updated_at = ...

    def __str__(self):
        return self.id


