from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.

def login_view(request):
    return render(request, 'seller/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/home/")   


def validate_login(request):
    username = request.POST.get("username")
    user = authenticate(request=request,
                        username=username,
                        password=request.POST.get("password"))
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/seller/"+username+"/")
    else:
        return HttpResponseRedirect("/seller/login/")


def validate_create(request):
    print("validate_create")
    username = request.POST.get("username")
    try:
        user = User.objects.get(username=username)
        print("Username not available")
        return HttpResponseRedirect("/seller/create/")
    except User.DoesNotExist:
        user = User.objects.create_user(username=username,
                                        email=request.POST.get("email"),
                                        password=request.POST.get("password"))
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()
        login(request, user)
        return HttpResponseRedirect("/seller/"+username+"/")


def create(request):
    return render(request, 'seller/create.html') 


def seller_home(request, username):
    context = {'full_name':request.user.get_full_name()}
    return render(request, 'seller/home.html', context)


def add_product(request, username):
    seller_name = "Vinushan"
    seller_location = "Wellawatte"
    seller_phone = "0775325237"
    context = {'username':request.user.username,
               'full_name':request.user.get_full_name(),
               'seller_name':seller_name,
               'location':seller_location,
               'phone':seller_phone}
    return render(request, 'seller/addproduct.html', context)