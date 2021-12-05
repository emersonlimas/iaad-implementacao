from django.shortcuts import render, redirect
from app.forms import CLINICAForm, ESPECIALIDADEForm, MEDICOForm, PACIENTEForm, AGENDACONSULTAForm, CLINICAMEDICOForm
from app.models import CLINICA, CLINICAMEDICO, ESPECIALIDADE, MEDICO, PACIENTE, AGENDACONSULTA
from django.db import connection
from django.core.paginator import Paginator
# Read------------------------------------------------------------------------


def home(request):
    return render(request, 'index.html')


def tab_clinica(request):
    data = {}
    search = request.GET.get('search')
    if search:
        filtrado = CLINICA.objects.filter(NomeCli__icontains=search)
        paginator = Paginator(filtrado, 2)
        pages = request.GET.get('page')
        data['clinica'] = paginator.get_page(pages)

    else:
        #data['clinica'] = CLINICA.objects.all()
        all = CLINICA.objects.all()
        paginator = Paginator(all, 2)
        pages = request.GET.get('page')
        data['clinica'] = paginator.get_page(pages)

    return render(request, 'tab_clinica.html', data)


def tab_espec(request):
    data = {}
    search = request.GET.get('search')
    if search:
        filtrado = ESPECIALIDADE.objects.filter(NomeEspec__icontains=search)
        paginator = Paginator(filtrado, 2)
        pages = request.GET.get('page')
        data['especialidade'] = paginator.get_page(pages)

    else:
        all = ESPECIALIDADE.objects.all()
        paginator = Paginator(all, 2)
        pages = request.GET.get('page')
        data['especialidade'] = paginator.get_page(pages)

    return render(request, 'tab_espec.html', data)


def tab_med(request):
    data = {}
    search = request.GET.get('search')
    if search:
        filtrado = MEDICO.objects.filter(NomeMed__icontains=search)
        paginator = Paginator(filtrado, 2)
        pages = request.GET.get('page')
        data['medico'] = paginator.get_page(pages)

    else:
        all = MEDICO.objects.all()
        paginator = Paginator(all, 2)
        pages = request.GET.get('page')
        data['medico'] = paginator.get_page(pages)

    return render(request, 'tab_med.html', data)


def tab_pac(request):
    data = {}
    search = request.GET.get('search')
    if search:
        filtrado = PACIENTE.objects.filter(NomePac__icontains=search)
        paginator = Paginator(filtrado, 2)
        pages = request.GET.get('page')
        data['paciente'] = paginator.get_page(pages)

    else:
        all = PACIENTE.objects.all()
        paginator = Paginator(all, 2)
        pages = request.GET.get('page')
        data['paciente'] = paginator.get_page(pages)

    return render(request, 'tab_pac.html', data)


def tab_agenda(request):
    data = {}
    search = request.GET.get('search')
    if search:
        filtrado = AGENDACONSULTA.objects.filter(CpfPaciente__icontains=search)
        paginator = Paginator(filtrado, 2)
        pages = request.GET.get('page')
        data['agenda'] = paginator.get_page(pages)

    else:
        all = AGENDACONSULTA.objects.all()
        paginator = Paginator(all, 2)
        pages = request.GET.get('page')
        data['agenda'] = paginator.get_page(pages)

    return render(request, 'tab_agenda.html', data)


def tab_climed(request):
    data = {}
    search = request.GET.get('search')
    if search:
        filtrado = CLINICAMEDICO.objects.filter(CodCli__icontains=search)
        paginator = Paginator(filtrado, 2)
        pages = request.GET.get('page')
        data['climed'] = paginator.get_page(pages)

    else:
        all = CLINICAMEDICO.objects.all()
        paginator = Paginator(all, 2)
        pages = request.GET.get('page')
        data['climed'] = paginator.get_page(pages)

    return render(request, 'tab_climed.html', data)


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


def form_climed(request):
    data = {}
    data['form_climed'] = CLINICAMEDICOForm()
    return render(request, 'form_climed.html', data)

# VIEW--------------------------------------------------------------------------


def view_clinica(request, pk):
    data = {}
    data['clinica'] = CLINICA.objects.get(pk=pk)
    return render(request, 'view_clinica.html', data)


def view_espec(request, pk):
    data = {}
    data['especialidade'] = ESPECIALIDADE.objects.get(pk=pk)
    return render(request, 'view_espec.html', data)


def view_pac(request, pk):
    data = {}
    data['paciente'] = PACIENTE.objects.get(pk=pk)
    return render(request, 'view_pac.html', data)


def view_med(request, pk):
    data = {}
    data['medico'] = MEDICO.objects.get(pk=pk)
    return render(request, 'view_med.html', data)


def view_agenda(request, pk):
    data = {}
    data['agenda'] = AGENDACONSULTA.objects.get(pk=pk)
    return render(request, 'view_agenda.html', data)


def view_climed(request, pk):
    data = {}
    data['climed'] = CLINICAMEDICO.objects.get(pk=pk)
    return render(request, 'view_climed.html', data)


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


def create_climed(request):
    form = CLINICAMEDICOForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tab_climed')


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


def edit_agenda(request, pk):
    data = {}
    data['agenda'] = AGENDACONSULTA.objects.get(pk=pk)
    data['form_agenda'] = AGENDACONSULTAForm(instance=data['agenda'])
    return render(request, 'form_agenda.html', data)


def edit_climed(request, pk):
    data = {}
    data['climed'] = CLINICAMEDICO.objects.get(pk=pk)
    data['form_climed'] = CLINICAMEDICOForm(instance=data['climed'])
    return render(request, 'form_climed.html', data)


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


def update_agenda(request, pk):
    data = {}
    data['agenda'] = AGENDACONSULTA.objects.get(pk=pk)
    form = AGENDACONSULTAForm(request.POST or None, instance=data['agenda'])
    if form.is_valid():
        form.save()
        return redirect('tab_agenda')


def update_climed(request, pk):
    data = {}
    data['climed'] = CLINICAMEDICO.objects.get(pk=pk)
    form = CLINICAMEDICOForm(request.POST or None, instance=data['climed'])
    if form.is_valid():
        form.save()
        return redirect('tab_climed')


# DELETE------------------------------------------------------------


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


def delete_climed(request, pk):
    climed = CLINICAMEDICO.objects.get(pk=pk)
    climed.delete()
    return redirect('tab_climed')


# DELETE ALL------------------------------------------------------------
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


def delete_all_climed(request):
    cursor.execute('call excluir_climed')
    result = cursor.fetchall()
    return render(request, 'tab_climed.html', {'result': result})
