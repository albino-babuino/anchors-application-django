from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    image = models.ImageField(upload_to='category', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta: #Metadatos de la clase
        verbose_name = 'Categoría' #Con este nombre se mostrará en el panel de administración
        verbose_name_plural = 'Categorías' #Con este nombre se mostrará en el panel de administración

    def __str__(self):
        return self.name
    
class Anchor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    link = models.CharField(max_length=250, verbose_name='Enlace')
    image = models.ImageField(upload_to='anchor', verbose_name='Imagen')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta: #Metadatos de la clase
        verbose_name = 'Enlace' #Con este nombre se mostrará en el panel de administración
        verbose_name_plural = 'Enlaces' #Con este nombre se mostrará en el panel de administración

    def __str__(self):
        return self.name

