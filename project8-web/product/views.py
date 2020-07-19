from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def list_all(request, location_id):
    return HttpResponse(status=200)


def product_page(request, product_id):
    return HttpResponse(status=200)


def add_product(request):
    return HttpResponseRedirect("/seller/"+request.user.username+"/")