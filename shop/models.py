from django.db import models


class Category(models.Model):
    title = ...
    show_in_menu = ...

    def __str__(self):
        return self.title


class Product(models.Model):
    title = ...
    price = ...
    count = ...
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name=...)

    def __str__(self):
        return self.title

