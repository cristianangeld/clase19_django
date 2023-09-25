from django import forms
from .models import Curso

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'comision']


    def clean_comision(self):
        comision = self.cleaned_data.get('comision')
        if comision > 50000:
            raise forms.ValidationError("La comisión no puede ser mayor de 50000.")
        return comision

