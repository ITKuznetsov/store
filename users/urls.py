from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', login_required(views.UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', views.EmailVerificationView.as_view(), name='verify'),
]