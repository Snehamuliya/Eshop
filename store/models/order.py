import datetime

from django.db import models
from .product import Product
from .customer import Customer


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.CharField(max_length=20, default='', blank=True)
    address = models.CharField(max_length=300, default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer =  customer_id)\
            .order_by('-date')

