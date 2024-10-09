import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Anchor

class Index(ListView):
    queryset = Category.objects.all().order_by('name')
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
        category = self.object

        # Obtener el término de búsqueda desde la solicitud GET
        search_query = self.request.GET.get('query', '')
        reset_search = self.request.GET.get('reset', '')

        # Si el botón de reset se presiona, limpiar el campo de búsqueda
        if reset_search == 'reset':
            # Formulario vacío al resetear
            form = SearchAnchorForm()  # Se crea un formulario sin datos
            anchors = Anchor.objects.filter(category=category)
        elif search_query:
            # Si hay búsqueda, filtrar los anchors
            anchors = Anchor.objects.filter(category=category, name__icontains=search_query)
            form = SearchAnchorForm(self.request.GET)  # Se mantiene el término en el campo de búsqueda
        else:
            # Mostrar todos los anchors si no hay búsqueda
            anchors = Anchor.objects.filter(category=category)
            form = SearchAnchorForm()  # Formulario vacío

        # Añadir el formulario y los anchors al contexto
        context['form'] = form
        context['anchors'] = anchors
        return context
