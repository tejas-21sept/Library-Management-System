from enum import unique
from rest_framework import serializers
#from django.contrib.auth.models import AbstractUser as User
from .models import CustomUser 
from .models import Book

class RegisterSerializer(serializers.ModelSerializer):
  is_staff = serializers.BooleanField(default=True)
  
  class Meta:
    model = CustomUser
    fields = ['username', 'password','email','is_superuser','is_staff']
    
  def create(self,validated_data):
    user = CustomUser.objects.create(username=validated_data['username'])
    user.email = validated_data['email']
    user.set_password(validated_data['password'])
    user.is_superuser = validated_data['is_superuser']
    user.is_staff = validated_data['is_superuser']
    user.save()
    return user
    
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'  

    