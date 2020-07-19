from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def landing(request):
    if request.user.is_authenticated:
        context = {'logged_in':True}
    else:
        context = {'logged_in':False}
    return render(request, 'home/all.html', context)