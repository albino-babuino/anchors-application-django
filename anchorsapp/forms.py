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
            # Verifica si la imagen supera los 250 kB (250 * 1024 bytes)
            if image.size > 250 * 1024:  # 250 kB en bytes
                raise forms.ValidationError("El tamaño de la imagen no debe exceder los 250 kB.")
            
            # Verifica la extensión del archivo
            file_extension = image.name.split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'gif', 'webp', 'png']:  # Agregado 'png'
                raise forms.ValidationError("Solo se permiten archivos con formatos .jpg, .jpeg, .gif, .webp y .png.")
        
        return image

class AnchorForm(forms.ModelForm):
    class Meta:
        model = Anchor
        fields = ['name', 'link', 'image']  # Excluir 'category' de los campos del formulario

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Verifica si la imagen supera los 250 kB (250 * 1024 bytes)
            if image.size > 250 * 1024:  # 250 kB en bytes
                raise forms.ValidationError("El tamaño de la imagen no debe exceder los 250 kB.")
            
            # Verifica la extensión del archivo
            file_extension = image.name.split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'gif', 'webp', 'png']:  # Agregado 'png'
                raise forms.ValidationError("Solo se permiten archivos con formatos .jpg, .jpeg, .gif, .webp y .png.")
        
        return image


