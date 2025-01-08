from django.urls import path

from .views import ProductList, ProductDetail

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('', ProductList.as_view(), name='product_list'),
]