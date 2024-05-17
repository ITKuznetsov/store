from django.urls import path, include

from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', views.ProductModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
