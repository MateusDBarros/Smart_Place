from . import models
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'name', 'price']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TableNum
        fields = ['id', 'number']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id', 'tableNum', 'data']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemPedido
        fields = ['id', 'pedido', 'quantity']