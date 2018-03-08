from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.
from s0 import settings


class Category(models.Model):
    """Category for products"""
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(PolymorphicModel):
    """Bulk, Individual, or Rental product"""
    TYPE_CHOICES = {
        ('BulkProduct', 'Bulk Product'),
        ('IndividualProduct', 'Individual Product'),
        ('RentalProduct', 'Rental Product'),
    }
    STATUS_CHOICES = {
        ('A', 'Active'),
        ('I', 'Inactive'),
    }
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICES, default='A')
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def image_url(self):
        root = "catalog/media/products/"
        if len(self.images.all()) > 0:
            url = settings.STATIC_URL + root + self.images.all()[0].filename
            return url
        else:
            url = settings.STATIC_URL + root + "image_unavailable.gif"
            return url

    def image_urls(self):
        root = "catalog/media/products/"
        li = []
        if len(self.images.all()) > 0:
            for im in self.images.all():
                url = settings.STATIC_URL + root + im.filename
                li.append(url)
            return li
        else:
            url= settings.STATIC_URL + "catalog/media/products/image_unavailable.gif"
            li.append(url)
            return li




class BulkProduct(Product):
    TITLE = 'Bulk Product'
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()


class IndividualProduct(Product):
    TITLE = 'Individual Product'
    pid = models.TextField()


class RentalProduct(Product):
    TITLE = 'Rental Account'
    pid = models.TextField()
    max_rental_days = models.IntegerField(default=0)
    retire_date = models.DateField(null=True, blank=True)

class ProductImage(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    filename = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')



