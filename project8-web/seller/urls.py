from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('login/validate/', views.validate_login, name='validate_login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('create/', views.create, name='create'),
    path('create/validate/', views.validate_create, name='validate_create'),
    path('<username>/', views.seller_home, name='seller_home'),
    path('<username>/add/', views.add_product, name='add_product')
]

