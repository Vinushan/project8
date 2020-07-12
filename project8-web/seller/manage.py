from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
import home.views


def validate_login(request):
    username = request.POST.get("username")
    user = authenticate(request=request,
                        username=username,
                        password=request.POST.get("password"))
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/seller/"+username)
    else:
        return HttpResponseRedirect("/seller/login")


def validate_create(request):
    print("validate_create")
    username = request.POST.get("username")
    try:
        user = User.objects.get(username=username)
        print("Username not available")
        return HttpResponseRedirect("/seller/create")
    except User.DoesNotExist:
        user = User.objects.create_user(username=username,
                                        email=request.POST.get("email"),
                                        password=request.POST.get("password"))
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()
        login(request, user)
        return HttpResponseRedirect("/seller/"+username)


def logout(request):
    logout(request)
    return HttpResponseRedirect("/home")     


def create(request):
    return HttpResponse(status=200) 