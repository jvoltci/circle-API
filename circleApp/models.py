from django.db import models


class Category(models.Model):
    CategoryName = models.CharField(max_length=50)

class SubCategory(models.Model):
    SubCategoryName = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Products(models.Model):
    ProductName = models.CharField(max_length=100)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)