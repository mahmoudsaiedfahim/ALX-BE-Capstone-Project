from django.urls import path

from .views import ProductList, ProductDetail, ReviewList, CategoryList

urlpatterns = [
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('products/<int:product_id>/reviews/', ReviewList.as_view(), name='review_list'),
]