from django.db import models
from django.contrib.auth.models import User
from productApp.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("Shipped", "Shipped"),
            ("Delivered", "Delivered")
        ],
        default="Pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
