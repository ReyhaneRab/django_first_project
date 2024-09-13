from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    show_in_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.BigIntegerField()
    count = models.IntegerField()
    isbn = models.BigIntegerField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name=...)

    def __str__(self):
        return self.title

