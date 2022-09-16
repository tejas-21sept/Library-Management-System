from django.db import models 
from django.contrib.auth.models import AbstractUser 

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    
    def __str__(self):
    	return self.name
 
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)