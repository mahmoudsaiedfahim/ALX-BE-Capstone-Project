from rest_framework import serializers
from .models import Category, Product , Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'stock_quantity',
            'image_url',
            'created_date'
            ]
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','rating','comment', 'created_at']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']