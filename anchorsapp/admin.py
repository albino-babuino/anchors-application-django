from django.contrib import admin
from .models import Category, Anchor

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created', 'updated')  # Asegúrate de que 'created' y 'updated' estén en el modelo
    search_fields = ('name',)  # Permitir búsqueda por nombre
    list_filter = ('user', 'created')  # Filtros por usuario y fecha de creación
    ordering = ('created',)  # Ordenar por fecha de creación

class AnchorAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'user', 'category', 'created', 'updated')  # Asegúrate de que 'created' y 'updated' estén en el modelo
    search_fields = ('name', 'link')  # Permitir búsqueda por nombre y enlace
    list_filter = ('user', 'category', 'created')  # Filtros por usuario, categoría y fecha de creación
    ordering = ('created',)  # Ordenar por fecha de creación

admin.site.register(Category, CategoryAdmin)
admin.site.register(Anchor, AnchorAdmin)
