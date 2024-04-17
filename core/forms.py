from django import forms 
from .models import Eventos

class EventoForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = '__all__'