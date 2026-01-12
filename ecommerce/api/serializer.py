from rest_framework import serializers
from ecommerce import models


class ProductSerializer(serializers.ModelSerializer):
    Category  = serializers.StringRelatedField()
    class Meta:
        model = models.Product
        fields = '__all__'
        
        
class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        fields = '__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields =  ['product', 'quantity']
        
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be greater than zero."
            )
        return value
        
    
    
        
    