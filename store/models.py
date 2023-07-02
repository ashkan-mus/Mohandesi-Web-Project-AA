from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES=(
    ('ps','Peste'),
    ('bh','Badoom-Hendi'),
    ('gr','Gerdoo'),
    ('fn','Fandogh'),
    ('tk','Tokhme'),
    ('bd','Bdoom-Derakhti'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    weight = models.FloatField()
    description = models.TextField()
    types = models.TextField(default='')
    category = models.CharField( choices = CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to= 'product')
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    locality = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Card(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


class Payment(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    amount =models.FloatField()
    razorpay_order_id  = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id  = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price