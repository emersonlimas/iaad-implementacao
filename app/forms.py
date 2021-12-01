from django.db.models import fields
from django.forms import ModelForm
from app.models import AGENDACONSULTA, CLINICA, CLINICAMEDICO, ESPECIALIDADE, MEDICO, PACIENTE


class CLINICAForm(ModelForm):  
    class Meta:
        model = CLINICA
        fields = ['CodCli', 'NomeCli', 'Endereco', 'Telefone', 'Email']



class ESPECIALIDADEForm(ModelForm):
    class Meta:
        model = ESPECIALIDADE
        fields = ['CodEspec', 'NomeEspec', 'Descricao']


class MEDICOForm(ModelForm):
    class Meta:
        model = MEDICO
        fields = ['CodMed', 'NomeMed', 'Genero', 'Telefone', 'Email', 'CodEspec']


class PACIENTEForm(ModelForm):
    class Meta:
        model = PACIENTE
        fields = ['CpfPaciente', 'NomePac', 'DataNascimento', 'Genero', 'Telefone', 'Email']


class AGENDACONSULTAForm(ModelForm):
    class Meta:
        model = AGENDACONSULTA
        fields = ['CodCli', 'CodMed', 'CpfPaciente', 'Data']

class CLINICAMEDICOForm(ModelForm):
    class Meta:
        model = CLINICAMEDICO
        fields = ['CodCli', 'CodMed', 'DataIngresso', 'CargaHorariaSemanal']