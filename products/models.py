from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254) 
    name = models.CharField(max_length=254)
    product_description = models.TextField()
    image = models.ImageField(blank=True,null=True)
    
    def __str__(self):
        return self.name

class sub_categories(models.Model):
   
    class Meta:
        verbose_name_plural = 'sub_categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def sub_categories_display_name(self):
        return self