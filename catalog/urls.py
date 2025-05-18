from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('product/add/', views.add_product_view, name='add_product'),
    path('product/<int:pk>/edit/', views.edit_product_view, name='edit_product'),
    path('product/<int:pk>/delete/', views.delete_product_view, name='delete_product'),
]
