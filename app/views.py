from django.shortcuts import render, redirect
from app.forms import CLINICAForm, ESPECIALIDADEForm, MEDICOForm, PACIENTEForm, AGENDACONSULTAForm
from app.models import CLINICA, ESPECIALIDADE, MEDICO, PACIENTE, AGENDACONSULTA

#Read------------------------------------------------------------------------
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


def tab_med(request):
    data = {}
    data['medico'] = MEDICO.objects.all()
    return render(request, 'tab_med.html', data)


def tab_pac(request):
    data = {}
    data['paciente'] = PACIENTE.objects.all()
    return render(request, 'tab_pac.html', data)


def tab_agenda(request):
    data = {}
    data['agenda'] = AGENDACONSULTA.objects.all()
    return render(request, 'tab_agenda.html', data)


#FORM------------------------------------------------------------------------
def form_clinica(request): 
    data = {}
    data['form_clinica'] = CLINICAForm()
    return render(request, 'form_clinica.html', data)


def form_espec(request): 
    data = {}
    data['form_espec'] = ESPECIALIDADEForm()
    return render(request, 'form_espec.html', data)


def form_med(request): 
    data = {}
    data['form_med'] = MEDICOForm()
    return render(request, 'form_med.html', data) 


def form_pac(request): 
    data = {}
    data['form_pac'] = PACIENTEForm()
    return render(request, 'form_pac.html', data) 


def form_agenda(request): 
    data = {}
    data['form_agenda'] = AGENDACONSULTAForm()
    return render(request, 'form_agenda.html', data)


#CREATE------------------------------------------------------------------------
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


def create_med(request):
    form = MEDICOForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('form_med')


def create_pac(request):
    form = PACIENTEForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('form_pac')


def create_agenda(request):
    form = AGENDACONSULTAForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('form_agenda')

