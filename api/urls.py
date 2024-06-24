from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', views.ProductModelViewSet)
router.register(r'baskets', views.BasketModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
