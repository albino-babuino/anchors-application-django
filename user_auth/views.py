from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, View
from django.contrib.auth import views as auth_views

class HomePage(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')  # Redirige a /categories si el usuario está autenticado
        return render(request, 'user_auth/home.html')
    
class CustomLoginView(auth_views.LoginView):
    template_name = 'user_auth/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')  # Redirigir a /categories si ya está autenticado
        return super().dispatch(request, *args, **kwargs)
    
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')  # Redirigir a /categories si ya está autenticado
        return super().dispatch(request, *args, **kwargs)
