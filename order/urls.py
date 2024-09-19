from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order/<int:product_id>/', views.add_to_order, name='add_to_order'),

    path('view-order/', views.view_order, name='view_order'),

    path('complete-order/', views.complete_order, name='complete_order'),
]
