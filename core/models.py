from unittest.util import _MAX_LENGTH
from django.db import models

class Paciente(models.Model):
    nome = models.CharField('Nome: ', max_length=200)
    data_nasc = models.DateField('Data de nascimento: ')
    sexo = models.CharField('Sexo: ', max_length=1)
    relatorio_medico = models.CharField('Relatório médico: ', max_length=500)
    tratamento = models.CharField('Tratamento: ', max_length=500)
    naturalidade = models.CharField('Naturalidade (Cidade/Estado/País): ', max_length=300)
    cpf = models.CharField('CPF: ', max_length=11)
    tipo_sang = models.CharField('Tipo Sanguíneo: ', max_length=3)
    foto = models.ImageField(null=True, blank=True, upload_to="images/")

class Medicos(models.Model):
    nome = models.CharField('Nome: ', max_length=200)
    data_nasc = models.DateField('Data de nascimento: ')
    sexo = models.CharField('Sexo: ', max_length=1)
    especialidade = models.CharField('Especialidade: ', max_length=100)
    naturalidade = models.CharField('Naturalidade (Cidade/Estado/País): ', max_length=300)
    cpf = models.CharField('CPF: ', max_length=11)
    tipo_sang = models.CharField('Tipo Sanguíneo: ', max_length=3)
    foto = models.ImageField(null=True, blank=True, upload_to="images/")

class Fornecedores(models.Model):
    nome = models.CharField('Nome: ', max_length=200)
    produtos = models.CharField('Produtos: ', max_length=500)
    cnpj = models.CharField('CNPJ: ', max_length=14)
    localidade = models.CharField('Localidade (Cidade/Estado/País): ', max_length=300)