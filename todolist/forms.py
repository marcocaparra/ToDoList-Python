from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm): # Formulário para criar ou editar uma tarefa
    class Meta: # Meta class para definir o modelo e os campos do formulário
        model = Tarefa # Modelo associado ao formulário
        fields = ['tarefa', 'status'] # Campos do formulário
        widgets = { # Widgets para personalizar a aparência dos campos
            'tarefa': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = { # Rótulos para os campos do formulário
            'tarefa': 'Tarefa',
            'status': 'Status',
        }