from django.forms import ModelForm
from app.models import CLINICA

class CLINICAForm(ModelForm): #Chama um formulario
    class Meta:
        model = CLINICA
        fields = ['CodCli', 'NomeCli', 'Endereco', 'Telefone', 'Email']