from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views


class CustomLoginView(auth_views.LoginView):
    template_name = 'user_auth/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')  # Redirigir a /categories si ya está autenticado
        return super().dispatch(request, *args, **kwargs)
    
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy('categories')  # Redirigir a categorías tras el registro y login automático

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')  # Redirigir a /categories si ya está autenticado
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Este método es llamado cuando el formulario es válido (usuario registrado correctamente)."""
        response = super().form_valid(form)  # Crea el usuario

        # Autenticamos al usuario
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')  # `password1` es el campo del primer password en UserCreationForm
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)  # Inicia sesión automáticamente

        return response
