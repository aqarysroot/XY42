from rest_framework import serializers
from .models import Order, OrderItem
from catalogs.serializers import ProductSerializer
class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
    def to_representation(self, instance):
        representation = super(OrderItemsSerializer, self).to_representation(instance)
        representation["product"] = ProductSerializer(instance.product).data
        return representation

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        representation["items"] = OrderItemsSerializer(instance.items, many=True).data
        return representation

    