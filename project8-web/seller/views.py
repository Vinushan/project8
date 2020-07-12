from django.shortcuts import render
from django.http import HttpResponse
import home.urls

# Create your views here.

def login(request):
    return render(request, 'seller/login.html')


def create(request):
    return render(request, 'seller/create.html') 


def seller_home(request, username):
    return render(request, 'seller/home.html')


def add_product(request, username):
    return HttpResponse(status=200)