from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('<seller_id>/', views.seller_home, name='seller_home'),
    path('<seller_id>/new', views.add_product, name='add_product'),
]