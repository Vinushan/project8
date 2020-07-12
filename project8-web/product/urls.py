from django.urls import path

from . import views

urlpatterns = [
    path('all/<location_id>', views.list_all, name='list_all'),
    path('<product_id>/', views.product_page, name='product_page'),
]