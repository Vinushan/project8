from django.shortcuts import render
from django.http import HttpResponse
import home.urls

# Create your views here.

def login(request):
    return render(request, 'seller/login.html')

def logout(request):
    return home.views.landing(request)

def create(request):
    return render(request, 'seller/create.html') 

def seller_home(request, seller_id):
    return HttpResponse(status=200)

def add_product(request, seller_id):
    return HttpResponse(status=200)