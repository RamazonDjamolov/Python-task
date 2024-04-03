from django.db import models


# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = "Shops"


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True,  related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=30, decimal_places=3)
    image = models.ImageField(upload_to='product/images')
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"