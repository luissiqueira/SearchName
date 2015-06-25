from django import forms
from .models import Entity


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['number', 'name']
        widgets = {
            'number': forms.TextInput(attrs={'readonly': True, 'col': 80}),
        }