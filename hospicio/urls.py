"""hospicio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import cadastrar_fornecedor, cadastrar_medico, editar_fornecedor, editar_medico, listar_fornecedores, listar_pacientes, cadastrar_paciente, editar_paciente, remover_fornecedor, remover_medico, remover_paciente, listar_medicos, central

urlpatterns = [
    path('pacientes/', listar_pacientes, name='listar_pacientes'),
    path('paciente_cadastrar/', cadastrar_paciente, name='cadastrar_paciente'),
    path('paciente_editar/<int:id>/', editar_paciente, name='editar_paciente'),
    path('paciente_remover/<int:id>', remover_paciente, name='remover_paciente'),

    path('medicos/', listar_medicos, name='listar_medicos'),
    path('medico_cadastrar/', cadastrar_medico, name='cadastrar_medico'),
    path('medico_editar/<int:id>/', editar_medico, name='editar_medico'),
    path('medico_remover/<int:id>', remover_medico, name='remover_medico'),

    path('fornecedores/', listar_fornecedores, name='listar_fornecedores'),
    path('fornecedor_cadastrar/', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedor_editar/<int:id>/', editar_fornecedor, name='editar_fornecedor'),
    path('fornecedor_remover/<int:id>', remover_fornecedor, name='remover_fornecedor'),

    path('', central, name='sistema_hospicio'),

    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
