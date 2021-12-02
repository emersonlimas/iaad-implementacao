from django.shortcuts import render, redirect
from app.forms import CLINICAForm, ESPECIALIDADEForm, MEDICOForm, PACIENTEForm, AGENDACONSULTAForm
from app.models import CLINICA, ESPECIALIDADE, MEDICO, PACIENTE, AGENDACONSULTA
from django.db import connection  # IMPORTEI ESSA NOVA BIBLIOTECA

# Read------------------------------------------------------------------------


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


# FORM------------------------------------------------------------------------
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


# CREATE------------------------------------------------------------------------
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
        return redirect('tab_med')


def create_pac(request):
    form = PACIENTEForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tab_pac')


def create_agenda(request):
    form = AGENDACONSULTAForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tab_agenda')

# EDIT------------------------------------------------------------------------


def edit_clinica(request, pk):
    data = {}
    data['clinica'] = CLINICA.objects.get(pk=pk)
    data['form_clinica'] = CLINICAForm(instance=data['clinica'])
    return render(request, 'form_clinica.html', data)


def edit_espec(request, pk):
    data = {}
    data['especialidade'] = ESPECIALIDADE.objects.get(pk=pk)
    data['form_espec'] = ESPECIALIDADEForm(instance=data['especialidade'])
    return render(request, 'form_espec.html', data)


def edit_pac(request, pk):
    data = {}
    data['paciente'] = PACIENTE.objects.get(pk=pk)
    data['form_pac'] = PACIENTEForm(instance=data['paciente'])
    return render(request, 'form_pac.html', data)


def edit_med(request, pk):
    data = {}
    data['medico'] = MEDICO.objects.get(pk=pk)
    data['form_med'] = MEDICOForm(instance=data['medico'])
    return render(request, 'form_med.html', data)

# UPDATE------------------------------------------------------------------------


def update_clinica(request, pk):
    data = {}
    data['clinica'] = CLINICA.objects.get(pk=pk)
    form = CLINICAForm(request.POST or None, instance=data['clinica'])
    if form.is_valid():
        form.save()
        return redirect('tab_clinica')


def update_espec(request, pk):
    data = {}
    data['especialidade'] = ESPECIALIDADE.objects.get(pk=pk)
    form = ESPECIALIDADEForm(request.POST or None,
                             instance=data['especialidade'])
    if form.is_valid():
        form.save()
        return redirect('tab_espec')


def update_pac(request, pk):
    data = {}
    data['paciente'] = PACIENTE.objects.get(pk=pk)
    form = PACIENTEForm(request.POST or None, instance=data['paciente'])
    if form.is_valid():
        form.save()
        return redirect('tab_pac')


def update_med(request, pk):
    data = {}
    data['medico'] = MEDICO.objects.get(pk=pk)
    form = MEDICOForm(request.POST or None, instance=data['medico'])
    if form.is_valid():
        form.save()
        return redirect('tab_med')

# DELETE E DELETE ALL------------------------------------------------------------


def delete_clinica(request, pk):
    clinica = CLINICA.objects.get(pk=pk)
    clinica.delete()
    return redirect('tab_clinica')


def delete_espec(request, pk):
    espec = ESPECIALIDADE.objects.get(pk=pk)
    espec.delete()
    return redirect('tab_espec')


def delete_med(request, pk):
    med = MEDICO.objects.get(pk=pk)
    med.delete()
    return redirect('tab_med')


def delete_pac(request, pk):
    pac = PACIENTE.objects.get(pk=pk)
    pac.delete()
    return redirect('tab_pac')


def delete_agenda(request, pk):
    agenda = AGENDACONSULTA.objects.get(pk=pk)
    agenda.delete()
    return redirect('tab_agenda')


cursor = connection.cursor()  # ACRESCENTEI DAQUI PRA BAIXO


def delete_all_clinica(request):
    cursor.execute('call excluir_clinicas')
    result = cursor.fetchall()
    return render(request, 'tab_clinica.html', {'result': result})


def delete_all_espec(request):
    cursor.execute('call excluir_espec')
    result = cursor.fetchall()
    return render(request, 'tab_espec.html', {'result': result})


def delete_all_med(request):
    cursor.execute('call excluir_med')
    result = cursor.fetchall()
    return render(request, 'tab_med.html', {'result': result})


def delete_all_pac(request):
    cursor.execute('call excluir_pac')
    result = cursor.fetchall()
    return render(request, 'tab_pac.html', {'result': result})


def delete_all_agenda(request):
    cursor.execute('call excluir_agenda')
    result = cursor.fetchall()
    return render(request, 'tab_agenda.html', {'result': result})
