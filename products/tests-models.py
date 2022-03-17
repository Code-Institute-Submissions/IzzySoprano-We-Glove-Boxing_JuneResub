from django.test import TestCase
from .models import (
    Product, Gender, Category, SubCategory)


class TestProductsModels(TestCase):
    """
    Test the string methods return the correct model name fields
    """

    def test_products_string_method_returns_name(self):
        product = Product.objects.create(
            price=5.99,
            sku='abc123',
            name='Test Product',
            product_description='Test Product Description',
        )
        self.assertEqual(str(product), 'Test Product')

    def test_gender_string_method_returns_display_name(self):
        gender = Gender.objects.create(
            name='Test Gender',
            display_name='Test Display Name',
        )
        self.assertEqual(str(gender), 'Test Gender')

    def test_category_string_method_returns_display_name(self):
        master_category = MasterCategory.objects.create(
            name='Test Master Category',
            display_name='Test Display Name',
        )
        self.assertEqual(str(master_category), 'Test Master Category')

    def test_subcategory_method_returns_display_name(self):
        sub_category = SubCategory.objects.create(
            name='Test Sub Category',
            display_name='Test Display Name',
        )
        self.assertEqual(str(sub_category), 'Test Sub Category')