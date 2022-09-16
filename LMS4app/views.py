from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST,HTTP_200_OK
from rest_framework.views import APIView
from .serializers import RegisterSerializer,BookSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Book
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


class RegisterAPIView(APIView):
    """"
    For adding User in table. For performing CRUD operations on Book table, is_superuser must be set to True.
    """ 
    print("\nIn POST11\n")
    try:   
        def post(self, request):  
            
            serializer = RegisterSerializer(data=request.data)
            print(f"\nData==> {serializer} \n {serializer.is_valid()}") 
            print("\nIn POST\n")
            if serializer.is_valid():
                serializer.save()
                print("\nIn POST12\n")
                user = CustomUser.objects.get(username = serializer.data['username'])
                refresh = RefreshToken.for_user(user)
                return Response({"payload" : serializer.data,
                                "status":HTTP_201_CREATED,
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                                "message" : "User is created Successfully"})
            return Response({"status":HTTP_400_BAD_REQUEST,"payload" : serializer.errors,"message" : "User is not created Successfully"}) 
    
        """
        For getting the list of books using student login.
        """    
        def get(self, request):
            data = Book.objects.all()
            serializer = BookSerializer(data, many=True)
            return Response({"payload" : serializer.data,
                            "status":HTTP_200_OK})
    except:
        Response({"status":HTTP_400_BAD_REQUEST,"message" : "Please check credentials provided."})
        
        
class AuthenticateUserAPIView(APIView):
    """
    For performing CRUD operations on Book table but if only logged in using Admin/ Superuser credentials. 
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    try:   
        def get(self, request):     # Get the list of book
            data = CustomUser .objects.all()
            serializer = RegisterSerializer(data, many=True)
            return Response({"payload" : serializer.data,
                         "status":HTTP_200_OK})
         
        def post(self, request):    # Add a new book to list.
            serializer = BookSerializer(data=request.data)
            print(f"\nData==> {serializer}") 
            print("\nIn POST\n")
            if serializer.is_valid():
                serializer.save()

                return Response({"payload" : serializer.data,
                            "status":HTTP_201_CREATED,
                            "message" : "Book is added Successfully"})
            return Response({"status":HTTP_400_BAD_REQUEST,
                             "payload" : serializer.errors,
                             "message" : "User is not created Successfully"}) 
    
        
        def put(self, request):     # Update book information.
            serializer = BookSerializer(data=request.data)
            print(f"\nData==> {serializer}") 
            print("\nIn POST\n")
            if serializer.is_valid():
                serializer.save()

            return Response({"payload" : serializer.data,
                            "status":HTTP_201_CREATED,
                            "message" : "Book is updated Successfully"})
            
        def delete(self, request):  # Delete book record from table.
            data=request.data['id']
            obj1=Book.objects.get(pk=int(data))
            obj1.delete()
            print(f"\nData==> {type(data)}") 
            print("\nIn POST\n")
            return Response({
                            "status":HTTP_201_CREATED,
                            "message" : "Book is deleted Successfully"}) 
    except:
        Response({"status":HTTP_400_BAD_REQUEST,"message" : "Check Credentials"})
        
    
    
