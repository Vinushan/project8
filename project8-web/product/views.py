from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import api

# Create your views here.

def list_all(request, location_id):
    return HttpResponse(status=200)


def detail(request, product_id):
    return HttpResponse(status=200)


def add(request):
    response = api.add(request)
    return HttpResponseRedirect("/seller/"+request.user.username+"/")