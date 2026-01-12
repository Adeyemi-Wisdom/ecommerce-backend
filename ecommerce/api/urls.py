from django.urls import path, include
from ecommerce.api.views import ProductCreate, CategoryCreate, CategoryDetails,ReduceCartItemView,ProductDetails, AddToCartView, RemoveCartView

urlpatterns = [
    path('product/', ProductCreate.as_view(), name = 'Product-list'),
    path('category/', CategoryCreate.as_view(), name = 'Category-list'),
    path('product/<int:pk>/', ProductDetails.as_view(), name = 'Product-detail'),
    path('category/<int:pk>/', CategoryDetails.as_view(), name = 'Category-detail'),
    path('create-cart/', AddToCartView.as_view(), name = 'Add-to-cart'),
    path('remove-product/', RemoveCartView.as_view(), name = 'Remove-Product'),
    path('reduce-cart/', ReduceCartItemView.as_view(), name = 'Remove-Product'),
    
    
    
    
]