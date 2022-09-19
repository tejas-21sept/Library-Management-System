from itertools import product
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import *

# Create your views here.
def home(request):
    """
        Homepage to get the list of all available products in the database.
    """
    print("\nInside home function.\n")
    products = Product.objects.all()
    print(f"Products ==> {products}\n")
    context = {"products" : products}
    return render(request, 'ecomapp/home.html', context)

def register(request):
    """
        User registration function. Save user credentials in the database.
    """
    #print(request)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createUserForm()
        customerform = CustomerForm()
        
        if request.method == 'POST':
            form = createUserForm(request.POST)
            customerform = CustomerForm(request.POST)
            if form.is_valid() and customerform.is_valid():
                print("\nI'm in POST Register\n")
                user = form.save()
                customer = customerform.save(commit=False)
                customer.user = user
                customer.save()
                # user.save()
            return redirect('home') 
        context = {"adminform":form , "custform":customerform}     
        return render(request, 'ecomapp/register.html', context)
    
def loginpage(request):
    """
        User Login function, Retrive and validate user credentials to authenticate the user.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            print(f"\nRequest ==> {request.POST} \n") 
            username = request.POST['username'] 
            print(f"Uname ==> {username}\n")
            password = request.POST['password']
            user= log.debug(user.check_password(pw)) # Logs True!!!
            user = authenticate(request, username = username,password = password)
            print(f"user==> {user}")
            if user is not None:
                login(request,user)
                #return redirect('home') # check for after login page
                return HttpResponse("Login Success.")
        context = {}
        return render(request, 'ecomapp/login.html', context)
    
def logout(request):
    logout(request)
    return redirect('home') # Check for logout redirection

def placeorder(request,i):
    """
        Add elements in the perticular user's cart.
    """
    customer = Customer.objects.get(id=i)
    form = CreatOrderF()
    if request.method=="POST":
        form = CreatOrderF(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'ecomapp/placeorder.html', context)

def addProduct(request):
    """
        Add new products to display or available product's list.
    """
    form = ProductForm()
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'ecomapp/addProduct.html', context)
