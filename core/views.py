from sqlite3 import Cursor
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Fornecedores, Medicos, Paciente
from .forms import PacienteForm, MedicosForm, FornecedoresForm

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    contexto= {
        'todos_pacientes': pacientes
    }

    return render(request, 'pacientes.html', contexto)

def cadastrar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')

    form = PacienteForm
    contexto= {
        'form_paciente': form
    }
    return render(request, 'paciente_cadastrar.html', contexto)

def editar_paciente(request, id):
    paciente = Paciente.objects.get(pk=id)

    form = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)

    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')
    
    contexto = {
        'form_paciente': form
    }

    return render(request, 'paciente_cadastrar.html', contexto)

def remover_paciente(request, id):
    paciente = Paciente.objects.get(pk=id)
    paciente.delete()
    return redirect('listar_pacientes')


















def listar_medicos(request):
    medicos = Medicos.objects.all()
    contexto= {
        'todos_medicos': medicos
    }

    return render(request, 'medicos.html', contexto)

def cadastrar_medico(request):
    if request.method == "POST":
        form = MedicosForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('listar_medicos')

    form = MedicosForm
    contexto= {
        'form_medico': form
    }
    return render(request, 'medico_cadastrar.html', contexto)

def editar_medico(request, id):
    medico = Medicos.objects.get(pk=id)

    form = MedicosForm(request.POST or None, request.FILES or None, instance=medico)

    if form.is_valid():
        form.save()
        return redirect('listar_medicos')
    
    contexto = {
        'form_medico': form
    }

    return render(request, 'medico_cadastrar.html', contexto)

def remover_medico(request, id):
    medico = Medicos.objects.get(pk=id)
    medico.delete()
    return redirect('listar_medicos')






















def listar_fornecedores(request):
    fornecedor = Fornecedores.objects.all()
    contexto= {
        'todos_fornecedores': fornecedor
    }

    return render(request, 'fornecedores.html', contexto)

def cadastrar_fornecedor(request):
    form = FornecedoresForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_fornecedores')

    form = FornecedoresForm
    contexto= {
        'form_fornecedor': form
    }
    return render(request, 'fornecedor_cadastrar.html', contexto)

def editar_fornecedor(request, id):
    fornecedor = Fornecedores.objects.get(pk=id)

    form = FornecedoresForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('listar_fornecedores')
    
    contexto = {
        'form_fornecedor': form
    }

    return render(request, 'fornecedor_cadastrar.html', contexto)

def remover_fornecedor(request, id):
    fornecedor = Fornecedores.objects.get(pk=id)
    fornecedor.delete()
    return redirect('listar_fornecedores')










def central(request):
    return render(request, 'sistema_hospicio.html')