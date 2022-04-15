# Code adapted from the CI Boutique Ado mini project

from django.db import models

# Create your models here.


class Gender(models.Model):
    """
    Model Gender allows the grouping of product
    for easier searches
    """
    name = models.CharField(
        max_length=254)
    display_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def gender_display_name(self):
        return self.display_name


class Category(models.Model):
    "Creates category in database"
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    "Creates products in database"

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(
        'SubCategory', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    product_description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    gender = models.ForeignKey(
        'Gender', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    "Model SubCategory allows the grouping of products for easier searches by sub-category of product"

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def sub_categories_display_name(self):
        return self
