from django.shortcuts import render, redirect
from appiaad.forms import ClinicaForm, MedicoForm, PacienteForm, ClinicaMedicoForm, ConsultaForm, EspecialidadeForm
from appiaad.models import Clinica, Especialidade, ClinicaMedico


# telas de visualização
def home(request):
    data = {}
    data['db'] = Clinica.objects.all()
    return render(request, 'index.html', data)

def especialidades(request):
    data = {}
    data['db'] = Especialidade.objects.all()
    return render(request, 'especialidades.html', data)

def clinicamedico(request):
    data = {}
    data['db'] = ClinicaMedico.objects.all()
    return render(request, 'clinicamedico.html', data)

#formulários
def formclinica(request):
    data = {}
    data['formclinica'] = ClinicaForm()
    return render(request, 'formclinica.html', data)

def formmedico(request):
    data = {}
    data['formmedico'] = MedicoForm()
    return render(request, 'formmedico.html', data)

def formpaciente(request):
    data = {}
    data['formpaciente'] = PacienteForm()
    return render(request, 'formpaciente.html', data)

def formclinicamedico(request):
    data = {}
    data['formclinicamedico'] = ClinicaMedicoForm()
    return render(request, 'formclinicamedico.html', data)

def formconsulta(request):
    data = {}
    data['formconsulta'] = ConsultaForm()
    return render(request, 'formconsulta.html', data)

def formespecialidade(request):
    data = {}
    data['formespecialidade'] = EspecialidadeForm()
    return render(request, 'formespecialidade.html', data)

# create clínica
def createclinica(request):
    formclinica = ClinicaForm(request.POST or None)
    if formclinica.is_valid():
        formclinica.save()
        return redirect('home')

# create especialidade
def createespecialidade(request):
    formespecialidade = EspecialidadeForm(request.POST or None)
    if formespecialidade.is_valid():
        formespecialidade.save()
        return redirect('especialidades')

# create clinica/médico
def createclinicamedico(request):
    formclimedico = ClinicaMedicoForm(request.POST or None)
    if formclimedico.is_valid():
        formclimedico.save()
        return redirect('clinicamedico')