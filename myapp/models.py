from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=False)
    time_added = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    
    
# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    
    
    
    
    
    
    
    
    
#create a class called student
#with first name
#last name 
#phone number    
    
    #configuration for static files needs to be done in settings.py file and urls.py file for the static files to be served correctly.

    def __str__(self):
        return self.name