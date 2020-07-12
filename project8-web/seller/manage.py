from django.contrib.auth.models import User
from django.http import HttpResponse


def login(request):
    return HttpResponse(status=200)

def create(request):
    return HttpResponse(status=200) 