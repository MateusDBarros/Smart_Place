from django.shortcuts import render
from . import models, serializers
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

# Product Views
class ProductPost(generics.CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = 'pk'

class ProductDeleteAll(APIView):
    def delete(self, request):
        models.Product.objects.all().delete()
        return Response({'mensagem': 'Todos os produtos foram deletados.'}, status=status.HTTP_204_NO_CONTENT)

# Table Views
class TablePost(generics.CreateAPIView):
    queryset = models.TableNum.objects.all()
    serializer_class = serializers.TableSerializer

class TableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TableNum.objects.all()
    serializer_class = serializers.TableSerializer
    lookup_field = 'pk'

class TableDeleteAll(APIView):
    def delete(self, request):
        models.TableNum.objects.all().delete()
        return Response({'mensagem': 'Todas as mesas foram deletadas.'}, status=status.HTTP_204_NO_CONTENT)

# Order Views
class OrderPost(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field = 'pk'

class OrderDeleteAll(APIView):
    def delete(self, request):
        models.Order.objects.all().delete()
        return Response({'mensagem': 'Todos os pedidos foram deletados.'}, status=status.HTTP_204_NO_CONTENT)
