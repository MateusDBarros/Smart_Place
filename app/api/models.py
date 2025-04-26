from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    ## nome preco
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.name} - R${self.price:.2f}'

class TableNum(models.Model):
    number = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])

    def __str__(self):
        return f'Mesa Numero: {self.number} '
   
# Pedido cliente produto quantidade e data
class Order(models.Model):
    tableNum = models.ForeignKey(TableNum, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return f"Pedido Mesa {self.tableNum.number} - {self.data.strftime('%d/%m %H:%M')}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Order, related_name="itens", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"


