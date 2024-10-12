from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Relación con el usuario
    name = models.CharField(max_length=50, verbose_name='Nombre')
    image = models.ImageField(upload_to='category', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    bg_color = models.CharField(max_length=150, default='#0d1117', verbose_name='Color de fondo')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Anchor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Relación con el usuario
    name = models.CharField(max_length=50, verbose_name='Nombre')
    link = models.CharField(max_length=250, verbose_name='Enlace')
    image = models.ImageField(upload_to='anchor', verbose_name='Imagen')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'

    def __str__(self):
        return self.name
