from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Category, Anchor
from .forms import SearchAnchorForm, CategoryForm, AnchorForm
    
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
        category = self.object  # Obtiene la categoría actual

        # Obtener solo los anchors del usuario autenticado
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


class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'anchorsapp/create_category.html'
    success_url = '/categories/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Asignar el usuario autenticado
        return super().form_valid(form)

class CreateAnchor(LoginRequiredMixin, CreateView):
    model = Anchor
    form_class = AnchorForm
    template_name = 'anchorsapp/create_anchor.html'
    # Se elimina la línea success_url, ya que se configurará en get_success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        # Verificar que la categoría pertenece al usuario autenticado
        category = get_object_or_404(Category, pk=category_id, user=self.request.user)
        context['category'] = category  # Agregar la categoría al contexto
        return context

    def form_valid(self, form):
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id, user=self.request.user)
        form.instance.user = self.request.user  # Asignar el usuario logueado
        form.instance.category = category  # Asignar la categoría
        return super().form_valid(form)

    def get_success_url(self):
        # Redirigir a la página de detalles de la categoría después de crear el enlace
        return reverse_lazy('category_detail', args=[self.kwargs['category_id']])

# Vista para actualizar una categoría
class UpdateCategory(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'anchorsapp/update_category.html'
    success_url = reverse_lazy('categories')

    def get_object(self, queryset=None):
        # Asegurarse de que el usuario autenticado solo pueda actualizar sus categorías
        return get_object_or_404(Category, pk=self.kwargs['pk'], user=self.request.user)

# Vista para actualizar un enlace (anchor)
class UpdateAnchor(LoginRequiredMixin, UpdateView):
    model = Anchor
    form_class = AnchorForm
    template_name = 'anchorsapp/update_anchor.html'

    def get_object(self, queryset=None):
        # Asegurarse de que el usuario autenticado solo pueda actualizar sus enlaces
        return get_object_or_404(Anchor, pk=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        # Redirigir a la página de detalles de la categoría después de actualizar el enlace
        category_id = self.object.category.id  # Obtener la categoría del anchor actualizado
        return reverse_lazy('category_detail', args=[category_id])

# Vista para eliminar una categoría
class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'anchorsapp/delete_category.html'
    success_url = reverse_lazy('categories')

    def get_object(self, queryset=None):
        # Asegurarse de que el usuario autenticado solo pueda eliminar sus categorías
        return get_object_or_404(Category, pk=self.kwargs['pk'], user=self.request.user)

# Vista para eliminar un enlace (anchor)
class DeleteAnchor(LoginRequiredMixin, DeleteView):
    model = Anchor
    template_name = 'anchorsapp/delete_anchor.html'

    def get_object(self, queryset=None):
        # Asegurarse de que el usuario autenticado solo pueda eliminar sus propios enlaces
        return get_object_or_404(Anchor, pk=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        # Redirigir a la página de detalles de la categoría después de eliminar el enlace
        category_id = self.object.category.id  # Obtener la categoría del anchor eliminado
        return reverse_lazy('category_detail', args=[category_id])
    