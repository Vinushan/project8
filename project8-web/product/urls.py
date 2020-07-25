from django.urls import path

from . import views

urlpatterns = [
    path('all/<location_id>/', views.list_all, name='list_all'),
    path('add/', views.add, name='add'),
    path('<product_id>/', views.detail, name='detail')
]