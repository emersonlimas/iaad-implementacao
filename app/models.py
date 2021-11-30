from django.db import models

# Create your models here.


class CLINICA(models.Model):  # MODELO DE UMA UNICA TABELA (Sim, tenho duvidas também)
    CodCli = models.CharField(max_length=3, primary_key=True)
    NomeCli = models.CharField(max_length=130)
    Endereco = models.CharField(max_length=130)
    Telefone = models.CharField(max_length=11)
    Email = models.CharField(max_length=130)


class MEDICO(models.Model):
    CodMed = models.CharField(max_length=3, primary_key=True)
    NomeMed = models.CharField(max_length=130)
    Genero = models.CharField(max_length=1)
    Telefone = models.CharField(max_length=11)
    Email = models.CharField(max_length=130)
    CodEspec = models.CharField(max_length=3)


class PACIENTE(models.Model):
    CpfPaciente = models.CharField(max_length=11, primary_key=True)
    NomePac = models.CharField(max_length=130)
    DataNascimento = models.DateField()
    Genero = models.CharField(max_length=1)
    Telefone = models.CharField(max_length=11)
    Email = models.CharField(max_length=130)


class CLINICAMEDICO(models.Model):
    CodCli = models.CharField(max_length=3)
    CodMed = models.CharField(max_length=3)
    DataIngresso = models.DateField()
    CargaHorariaSemanal = models.CharField(max_length=3)


class AGENDACONSULTA(models.Model):
    CodCli = models.CharField(max_length=3)
    CodMed = models.CharField(max_length=3)
    CpfPaciente = models.CharField(max_length=11)
    Data = models.DateField()


class ESPECIALIDADE(models.Model):
    CodEspec = models.CharField(max_length=3, primary_key=True)
    NomeEspec = models.CharField(max_length=130)
    Descricao = models.CharField(max_length=130)