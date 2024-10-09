from django import forms

class SearchAnchorForm(forms.Form):
    query = forms.CharField(label='', max_length=50, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Buscar enlace...'
    }))
