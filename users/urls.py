from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.log, name='login'),
    path('registration/', views.reg, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]