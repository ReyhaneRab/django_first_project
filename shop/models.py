from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    show_in_menu = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.BigIntegerField()
    count = models.IntegerField()
    isbn = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    is_available = models.BooleanField(default=True)
    cover_image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

