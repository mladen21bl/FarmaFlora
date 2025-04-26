from django import forms
from .models import Plant, ActiveCompound

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'latin_name', 'image', 'description', 'drug', 'indications', 'regions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'latin_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={
                'rows': 3, 'class': 'form-control', 'style': 'resize: vertical;'
            }),
            'drug': forms.TextInput(attrs={'class': 'form-control'}),
            'indications': forms.Textarea(attrs={
                'rows': 3, 'class': 'form-control', 'style': 'resize: vertical;'
            }),
            'regions': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class ActiveCompoundForm(forms.ModelForm):
    class Meta:
        model = ActiveCompound
        fields = ['plants', 'name', 'mol_file', 'iupac_name', 'description', 'molecular_formula', 'solubility', 'structure_class']
        widgets = {
            'plants': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mol_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'iupac_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'molecular_formula': forms.TextInput(attrs={'class': 'form-control'}),
            'solubility': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'structure_class': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
