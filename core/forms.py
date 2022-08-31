from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Paciente, Medicos, Fornecedores

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nasc', 'sexo', 'relatorio_medico', 'tratamento', 'naturalidade', 'cpf', 'tipo_sang', 'foto']

class MedicosForm(ModelForm):
    class Meta:
        model = Medicos
        fields = ['nome', 'data_nasc', 'sexo', 'especialidade', 'naturalidade', 'cpf', 'tipo_sang', 'foto']

class FornecedoresForm(ModelForm):
    class Meta:
        model = Fornecedores
        fields = ['nome', 'produtos', 'cnpj', 'localidade']