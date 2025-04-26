from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from . import models

class OrderAPITest(APITestCase):

    def setUp(self):
        self.table = models.TableNum.objects.create(number=2)
        self.product = models.Product.objects.create(name='Café Latte', price=12.50)

    def test_create_order(self):
        url = reverse('order-post')  # certifique-se de que o nome da URL está certo!
        data = {
            'tableNum': self.table.id,  # precisa ser ID, não o objeto
            'product': self.product.id,
            'quantity': 2,
            'data': '2025-04-16T08:30:00Z'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_orders(self):
        order = models.Order.objects.create(
            tableNum=self.table,
            product=self.product,
            quantity=1,
            data='2025-04-16T08:30:00Z'
        )
        url = reverse('order-detail', args=[order.id])  # novamente, confira o nome da URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
