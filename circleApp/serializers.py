from rest_framework import serializers
from circleApp.models import Products, Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'CategoryName',)

class SubCategorySerializer(serializers.ModelSerializer):
    #category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'SubCategoryName', 'category',)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id', 'ProductName', 'subCategory',)