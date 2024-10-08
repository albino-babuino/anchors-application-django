from django.contrib import admin

from .models import Category, Anchor

#Para que aparezcan en el panel de administración de Django:
admin.site.register(Category)
admin.site.register(Anchor)