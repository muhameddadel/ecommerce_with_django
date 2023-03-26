from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null= True, blank= True)
    
    def __str__(self) -> str:
        return self.name
    
    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transation_id = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return str(self.id)
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    zipcode = models.CharField(max_length=50, null=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address