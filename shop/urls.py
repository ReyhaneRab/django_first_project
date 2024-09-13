from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_product, name='list_product'),
    path('products/detail/<int:product_id>/', views.detail_product, name='detail_product'),
    path('products/category/<int:category_id>/', views.list_product_for_category, name='list_product_for_category'),
]
