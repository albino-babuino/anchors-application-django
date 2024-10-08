import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Anchor

class Index(ListView):
    queryset = Category.objects.all()
    template_name = 'anchorsapp/index.html'
    context_object_name = 'category_object_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Category, Anchor
from .forms import SearchAnchorForm

class CategoryDetail(DetailView):
    model = Category
    template_name = 'anchorsapp/category_detail.html' 
    context_object_name = 'category_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener la categoría actual
        category = self.object
        
        # Obtener el término de búsqueda desde GET
        search_query = self.request.GET.get('query', '')

        # Crear el formulario de búsqueda
        form = SearchAnchorForm(self.request.GET)
        
        if search_query:
            # Filtrar los anchors basados en el término de búsqueda
            anchors = Anchor.objects.filter(category=category, name__icontains=search_query)
        else:
            # Mostrar todos los anchors si no hay término de búsqueda
            anchors = Anchor.objects.filter(category=category)

        # Añadir el formulario y los anchors al contexto
        context['form'] = form
        context['anchors'] = anchors
        return context
