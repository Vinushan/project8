from django.urls import path

from . import views

urlpatterns = [
    path('all/<location_id>/', views.list_all, name='list_all'),
    path('add/', views.add_product, name='add_product'),
    path('<product_id>/', views.product_page, name='product_page')
]