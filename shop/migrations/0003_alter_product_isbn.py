# Generated by Django 4.2.16 on 2024-09-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_cover_image_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
