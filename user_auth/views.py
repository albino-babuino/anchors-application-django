from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, View

class HomePage(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redirige a /categories si el usuario está autenticado
        return render(request, 'user_auth/home.html')
    

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy('login')
