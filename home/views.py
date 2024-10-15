from django.shortcuts import render, redirect
from django.views.generic import View

class HomePage(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('categories')  # Redirige a /categories si el usuario está autenticado
        return render(request, 'home/home.html')
    
