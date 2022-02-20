from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True) 
    name = models.CharField(max_length=254)
    product_description = models.TextField()
    image = models.ImageField(blank=True,null=True)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def sub_categories_display_name(self):
        return self