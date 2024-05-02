from . import views
from django.urls import path

app_name = 'orders'

urlpatterns = [
    path('order-create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order-created/', views.OrderSuccessView.as_view(), name='success'),
    path('', views.OrderListView.as_view(), name='orders'),
    path('order', views.OrderView.as_view(), name='order'),
]