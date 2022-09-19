from itertools import product
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import *

<<<<<<< HEAD

class RegisterAPIView(APIView):
    """"
    User registration method, save the data in the database after validating the data.
    For adding User in table. For performing CRUD operations on Book table, is_superuser must be set to True.
    """ 
    try:   
        def post(self, request):  
            
            serializer = RegisterSerializer(data=request.data)      # Serialize the user given data (JSON).
            if serializer.is_valid():                               # Validate the serialized data.
                serializer.save()                                   # If data validated successfully, save the data in the database.
                user = CustomUser.objects.get(username = serializer.data['username'])   # Use instance to create access and refresh token for authorisation.
                refresh = RefreshToken.for_user(user)
                return Response({"payload" : serializer.data,       # If validation is successfull, then return ACCESS and REFRESH tokens.
                                "status":HTTP_201_CREATED,
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                                "message" : "User is created Successfully"})
            # If validation is not succesfull then return error message.
            return Response({"status":HTTP_400_BAD_REQUEST,"payload" : serializer.errors,"message" : "User is not created Successfully"}) 
    
        """
        For getting the list of books using student login.
        Retrieve all the available book list from database.
        """    
        def get(self, request):
            data = Book.objects.all()           # Get all the books from database.
            serializer = BookSerializer(data, many=True)    # Deserialize the book data.
            return Response({"payload" : serializer.data,   # Return the deserialized data.
                            "status":HTTP_200_OK})
    except:
        Response({"status":HTTP_400_BAD_REQUEST,"message" : "Please check credentials provided."})
        
        
class AuthenticateUserAPIView(APIView):
    """
    For performing CRUD operations on Book table but if only logged in using Admin/ Superuser credentials. 
    After successfull authorization, perform the CRUD operations on database.
    """
    authentication_classes = [JWTAuthentication]    # JWT authentication class is used.
    permission_classes = [IsAuthenticated]          # Authentication with valid credentials required to get access.
    
    try:   
        def get(self, request):     # Get the list of book
            data = CustomUser .objects.all()        # If superuser, then only retrieve list of all users.
            serializer = RegisterSerializer(data, many=True)    # Deserialized the data.
            return Response({"payload" : serializer.data,       # Return the deserialized data.
                         "status":HTTP_200_OK})
         
        def post(self, request):    # Add a new book to list.
            serializer = BookSerializer(data=request.data)      # Serialize the user given data.
            if serializer.is_valid():                           # Validate the user given data.
                serializer.save()                               # If validated successfully, save the data into database.

                return Response({"payload" : serializer.data,   # If validated successfully, return responce with serialized data.
                            "status":HTTP_201_CREATED,
                            "message" : "Book is added Successfully"})
                
            return Response({"status":HTTP_400_BAD_REQUEST,     # If validation is unsuccessfull, return the error message.
                             "payload" : serializer.errors,
                             "message" : "User is not created Successfully"}) 
    
        
        def put(self, request):     # Update book information.
            serializer = BookSerializer(data=request.data)      # deserialize the user given data.
            if serializer.is_valid():                           # Validate the user given data.
                serializer.save()                               # If validated successfully, save the data into database.

                return Response({"payload" : serializer.data,    # If validated successfully, return responce with serialized data.
                            "status":HTTP_201_CREATED,
                            "message" : "Book is updated Successfully"})
            return Response({"status":HTTP_400_BAD_REQUEST,     # If validation is unsuccessfull, return the error message.
                             "payload" : serializer.errors,
                             "message" : "User is not created Successfully"})
            
        def delete(self, request):  # Delete book record from table.
            data=request.data['id']                         # Get the id of record.
            obj1=Book.objects.get(pk=int(data))                # retrieve data from database and create an object
            obj1.delete()                                   # delete data from database.
            return Response({
                            "status":HTTP_201_CREATED,      # Return success message.
                            "message" : "Book is deleted Successfully"}) 
    except:
        Response({"status":HTTP_400_BAD_REQUEST,"message" : "Check Credentials"}) 
