from django.urls import path

from . import views, manage

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/validate', manage.validate_login, name='validate_login'),
    path('logout/<username>', manage.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('create/validate', manage.validate_create, name='validate_create'),
    path('<username>/', views.seller_home, name='seller_home'),
    path('<username>/new', views.add_product, name='add_product'),
]

