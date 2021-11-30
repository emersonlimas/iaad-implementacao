from django.forms import ModelForm
from app.models import CLINICA  # ESPECIALIDADES


class CLINICAForm(ModelForm):  # Chama um formulario
    class Meta:
        model = CLINICA
        fields = ['CodCli', 'NomeCli', 'Endereco', 'Telefone', 'Email']


'''
class ESPECIALIDADEForm(ModelForm):
    class Meta:
        model = ESPECIALIDADE
        fields = ['CodEspec', 'NomeEspec', 'Descricao']
'''
