from django.db import models

# Create your models here.
from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    name = models.CharField(verbose_name='Category Name', max_length=64, unique=True)
    description = models.TextField(verbose_name='Description', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    #we can set other names for categories here, including different name for plural
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Product Name', max_length=128)
    image = models.ImageField(upload_to='Image', blank=True)
    short_desc = models.CharField(verbose_name='Short product description', max_length=120, blank=True)
    description = models.TextField(verbose_name='Product description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Amount', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

