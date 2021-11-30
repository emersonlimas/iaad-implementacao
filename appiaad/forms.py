from django.forms import ModelForm
from appiaad.models import Clinica, Medico, Paciente, ClinicaMedico, Consulta, Especialidade

# Create the form class.
class ClinicaForm(ModelForm):
    class Meta:
        model = Clinica
        fields = ['codcli', 'nomecli', 'enderecocli', 'telefonecli', 'emailcli']
    
class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['codmed', 'nomemed', 'generomed', 'telefonemed', 'emailmed', 'codespecmed']

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['cpfpac', 'nomepac', 'datanascimentopac', 'generopac', 'telefonepac', 'emailpac']

class ClinicaMedicoForm(ModelForm):
    class Meta:
        model = ClinicaMedico
        fields = ['codcli', 'codmed', 'dataingresso', 'cargahorariasemanal']

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['codcli', 'codmed', 'cpfpaciente', 'data']

class EspecialidadeForm(ModelForm):
    class Meta:
        model = Especialidade
        fields = ['codespec', 'nomeespec', 'descricao']