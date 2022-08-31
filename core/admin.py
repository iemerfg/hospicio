from django.contrib import admin
from .models import Paciente, Medicos

admin.site.register(Paciente)
admin.site.register(Medicos)