from django.contrib import admin
from .models import Product, Order, TableNum, ItemPedido

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(TableNum)
admin.site.register(ItemPedido)

# Register your models here.
