from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)  # Stores the customer’s name
    email = models.EmailField(unique=True)  # Stores the customer’s email, must be unique

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    # Associates the order with a customer. Deletes orders if the customer is deleted.
    order_date = models.DateTimeField(auto_now_add=True)  # Stores the date the order was created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Stores the total cost of the order

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
