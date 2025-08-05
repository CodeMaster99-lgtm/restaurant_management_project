from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def__str__(self):
        return self.name
class order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('CANCELLED', 'Canceled'),
        ('DELIVERED', Delivered),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyField(Menu)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_status = models.DecimalField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"order #{self.id} by {self.customer.username}"
