from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('products/category/<int:category_id>/', views.products, name='category'),
    path('products/page/<int:page_number>/', views.products, name='paginator'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]