from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        campo = ['title', 'Genero']
    
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

        