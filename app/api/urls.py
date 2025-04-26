from . import views
from django.urls import path

urlpatterns = [
    # Urls dos Produtos
    path('products/', views.ProductPost.as_view(), name='product-post'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    # Urls das Measas
    path('tables/', views.TablePost.as_view(), name='table-post'),
    path('tables/<int:pk>', views.TableDetailView.as_view(), name='table-detail'),

    # Urls dos pedidos
    path('order/', views.OrderPost.as_view(), name='order-post'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail')
]