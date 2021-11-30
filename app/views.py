from django.shortcuts import render, redirect
from app.forms import CLINICAForm, ESPECIALIDADEForm
from app.models import CLINICA, ESPECIALIDADE

#Read
def home(request):
    return render(request, 'index.html')


def tab_clinica(request):
    data = {}
    data['clinica'] = CLINICA.objects.all()
    return render(request, 'tab_clinica.html', data)


def tab_espec(request):
    data = {}
    data['especialidade'] = ESPECIALIDADE.objects.all()
    return render(request, 'tab_espec.html', data)


#FORM
def form_clinica(request): 
    data = {}
    data['form_clinica'] = CLINICAForm()
    return render(request, 'form_clinica.html', data)


def form_espec(request): 
    data = {}
    data['form_espec'] = ESPECIALIDADEForm()
    return render(request, 'form_espec.html', data)


#CREATE
def create_clinica(request):
    form = CLINICAForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tab_clinica')


def create_espec(request):
    form = ESPECIALIDADEForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tab_espec')

