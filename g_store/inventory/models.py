from django.db import models
from base.models import CustomUser



# Create your models here. 
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    count = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} purchased {self.quantity} {self.product.name}"
    