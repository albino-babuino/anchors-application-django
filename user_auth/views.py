from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib import messages


class CustomLoginView(auth_views.LoginView):
    template_name = 'user_auth/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')  # Redirigir a /categories si ya está autenticado
        return super().dispatch(request, *args, **kwargs)
    
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy('categories')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Este método es llamado cuando el formulario es válido."""
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        # Autenticamos al usuario
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            # Mensaje de éxito al registrar y loguear correctamente
            messages.success(self.request, f'Bienvenido/a, {username}, te has registrado exitosamente.')
        return response

    def form_invalid(self, form):
        """Este método es llamado cuando el formulario es inválido."""
        # Si el formulario no es válido, mostrar un mensaje de error
        messages.error(self.request, 'Por favor corrige los errores a continuación.')
        return super().form_invalid(form)
