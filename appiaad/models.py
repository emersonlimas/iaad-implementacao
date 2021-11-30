from django.db import models

# Create your models here.
class Clinica(models.Model):
    codcli = models.IntegerField()
    nomecli = models.CharField(max_length=300)
    enderecocli = models.CharField(max_length=300)
    telefonecli = models.CharField(max_length=300)
    emailcli = models.EmailField()

class Medico(models.Model):
    codmed = models.IntegerField()
    nomemed = models.CharField(max_length=300)
    generomed = models.CharField(max_length=300)
    telefonemed = models.CharField(max_length=300)
    emailmed = models.EmailField()
    codespecmed = models.IntegerField()

class Paciente(models.Model):
    cpfpac = models.IntegerField()
    nomepac = models.CharField(max_length=300)
    datanascimentopac = models.DateField()
    generopac = models.CharField(max_length=300)
    telefonepac = models.CharField(max_length=300)
    emailpac = models.EmailField()

class ClinicaMedico(models.Model):
    codcli = models.IntegerField()
    codmed = models.IntegerField()
    dataingresso = models.CharField(max_length=300)
    cargahorariasemanal = models.CharField(max_length=300)

class Consulta(models.Model):
    codcli = models.IntegerField()
    codmed = models.IntegerField()
    cpfpaciente = models.IntegerField()
    data = models.DateField()

class Especialidade(models.Model):
    codespec = models.IntegerField()
    nomeespec = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300)