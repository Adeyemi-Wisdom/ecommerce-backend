from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    Name = models.CharField(max_length=500)
    About = models.CharField(max_length=200)
  
    
    def __str__(self):
        return self.Name
        

class Product(models.Model):
    Name = models.CharField(max_length=40, default='Product')
    Description = models.CharField(max_length=500)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(default=0)
    Is_available = models.BooleanField(default=True)
    Created_at = models.DateTimeField(default=timezone.now)
    Updated_at = models.DateTimeField(default=timezone.now)
    Price = models.IntegerField()
    Product_Image = models.ImageField()

    def save(self, *args, **kwargs):
        self.Is_available = self.quantity > 0
        self.Updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Name
    
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name = 'cart'  )
    Is_active = models.BooleanField(default=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}'s Cart"
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name= 'ItemS')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    class Meta:
        unique_together = ('cart', 'product')
    
    
    
    

