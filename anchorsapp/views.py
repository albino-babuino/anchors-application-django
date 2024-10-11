import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, View, DeleteView, UpdateView

from .models import Category, Anchor
from .forms import SearchAnchorForm, CategoryForm, AnchorForm

class HomePage(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redirige a /categories si el usuario está autenticado
        return render(request, 'anchorsapp/home.html')
    
class Categories(LoginRequiredMixin, ListView):
    template_name = 'anchorsapp/categories.html'
    context_object_name = 'category_object_list'

    def get_queryset(self):
        # Filtrar categorías por el usuario logueado
        return Category.objects.filter(user=self.request.user).order_by('name')

class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'anchorsapp/category_detail.html'
    context_object_name = 'category_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object

        # Obtener solo los anchors del usuario
        search_query = self.request.GET.get('query', '')
        reset_search = self.request.GET.get('reset', '')

        if reset_search == 'reset':
            form = SearchAnchorForm()
            anchors = Anchor.objects.filter(category=category, user=self.request.user)
        elif search_query:
            anchors = Anchor.objects.filter(category=category, user=self.request.user, name__icontains=search_query)
            form = SearchAnchorForm(self.request.GET)
        else:
            anchors = Anchor.objects.filter(category=category, user=self.request.user)
            form = SearchAnchorForm()

        context['form'] = form
        context['anchors'] = anchors
        return context


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'anchorsapp/register.html'
    success_url = reverse_lazy('login')

class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'anchorsapp/create_category.html'
    success_url = '/categories/' 

class CreateAnchor(CreateView):
    model = Anchor
    form_class = AnchorForm
    template_name = 'anchorsapp/create_anchor.html'
    success_url = '/categories/'  

    # Vista para eliminar una categoría
class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'anchorsapp/delete_category.html'
    success_url = reverse_lazy('categories')  # Redirige a la lista de categorías después de eliminar

# Vista para eliminar un enlace (anchor)
class DeleteAnchor(LoginRequiredMixin, DeleteView):
    model = Anchor
    template_name = 'anchorsapp/delete_anchor.html'
    success_url = reverse_lazy('categories')  # Redirige a la lista de categorías después de eliminar

# Vista para actualizar una categoría
class UpdateCategory(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'anchorsapp/update_category.html'
    success_url = reverse_lazy('categories')  # Redirige a la lista de categorías después de actualizar

# Vista para actualizar un enlace (anchor)
class UpdateAnchor(LoginRequiredMixin, UpdateView):
    model = Anchor
    form_class = AnchorForm
    template_name = 'anchorsapp/update_anchor.html'
    success_url = reverse_lazy('categories')  # Redirige a la lista de categorías después de actualizar

