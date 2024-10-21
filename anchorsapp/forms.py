from django import forms
from .models import Category, Anchor

class SearchAnchorForm(forms.Form):
    query = forms.CharField(
        label='', 
        max_length=50, 
        required=False, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Buscar enlace...'
        })
    )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'bg_color']  # Campos incluidos en el formulario

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Verifica si la imagen supera los 0.5 MB (524288 bytes)
            if image.size > 0.5 * 1024 * 1024:  # 0.5 MB en bytes
                raise forms.ValidationError("El tamaño de la imagen no debe exceder los 0.5 MB.")
        return image

class AnchorForm(forms.ModelForm):
    class Meta:
        model = Anchor
        fields = ['name', 'link', 'image']  # Excluir 'category' de los campos del formulario

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Verifica si la imagen supera los 0.5 MB (524288 bytes)
            if image.size > 0.5 * 1024 * 1024:  # 0.5 MB en bytes
                raise forms.ValidationError("El tamaño de la imagen no debe exceder los 0.5 MB.")
        return image


