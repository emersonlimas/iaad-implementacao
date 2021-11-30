from django.shortcuts import render, redirect
from app.forms import CLINICAForm, ESPECIALIDADEForm


def home(request):
    return render(request, 'index.html')


def adicionar_clinica(request): #irei modificar o nome da função para 'form_clinica'
    data = {}
    data['adicionar_clinica'] = CLINICAForm()
    return render(request, 'adicionar_clinica.html', data)


def create_clinica(request):
    form = CLINICAForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

'''
def form_especialidade(request): #
    data = {}
    data['adicionar_especialidade'] = ESPECIALIDADEForm()
    return render(request, 'adicionar_especialidade.html', data)

 
def create_especialidade(request):
     form = ESPECIALIDADEForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
'''