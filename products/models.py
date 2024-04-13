from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=False)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.name} | {self.category.name}'
