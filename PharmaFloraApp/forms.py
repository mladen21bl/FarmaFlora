from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'latin_name', 'image', 'description', 'drug', 'indications']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%; resize: vertical;'}),
            'indications': forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%; resize: vertical;'}),
        }
