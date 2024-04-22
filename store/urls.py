from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
]
