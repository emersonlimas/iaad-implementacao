from django.db import models

# Create your models here.


class CLINICA(models.Model): #MODELO DE UMA UNICA TABELA (Sim, tenho duvidas também)
    CodCli = models.CharField(max_length=3)
    NomeCli = models.CharField(max_length=130)
    Endereco = models.CharField(max_length=130)
    Telefone = models.CharField(max_length=11)
    Email = models.CharField(max_length=130)