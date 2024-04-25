from django.urls import reverse_lazy
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from typing import Any
from common.views import TittleMixin

# Create your views here.

class UserLoginView(TittleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('products:index')
    title = 'Store - Авторизация'


class UserRegistrationView(TittleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация прошла успешно!'
    title = 'Store - Регистрация'


class UserProfileView(TittleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Store - Профиль'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, Any]:
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context