from django import forms
from .models import Category, Anchor

class SearchAnchorForm(forms.Form):
    query = forms.CharField(label='', max_length=50, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Buscar enlace...'
    }))

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'bg_color']  # Campos que quieres que el formulario incluya

class AnchorForm(forms.ModelForm):
    class Meta:
        model = Anchor
        fields = ['name', 'link', 'image', 'category']  # Campos del formulario
