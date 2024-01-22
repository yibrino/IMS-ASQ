from .views import ProductCreateView,ProductListView,ProductDetailView
from  django.urls import path,include

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create-product'),
    path('lists/', ProductListView.as_view(), name='list-products'),
        path('lists/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),

    # Add other URLs as needed
]