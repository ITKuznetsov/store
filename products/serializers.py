from rest_framework import serializers

from products.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')

    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())