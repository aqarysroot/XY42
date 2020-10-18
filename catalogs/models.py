from django.db import models

# Create your models here.
class Catalog(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    catalog_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='catalogs', null=True, blank=True)

    def __str__(self):
        return self.catalog_name

class Product(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='Product_catalog', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Products', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name