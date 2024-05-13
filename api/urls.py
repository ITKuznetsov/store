from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('product-list/', views.ProductListAPIView.as_view(), name='product_list'),
]
