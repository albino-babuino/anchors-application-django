from django import forms

class SearchAnchorForm(forms.Form):
    query = forms.CharField(label='Buscar anchor', max_length=50, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Buscar...'
    }))
