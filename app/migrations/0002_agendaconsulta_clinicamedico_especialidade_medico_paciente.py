# Generated by Django 3.2.9 on 2021-11-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AGENDACONSULTA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodCli', models.CharField(max_length=3)),
                ('CodMed', models.CharField(max_length=3)),
                ('CpfPaciente', models.CharField(max_length=11)),
                ('Data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CLINICAMEDICO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodCli', models.CharField(max_length=3)),
                ('CodMed', models.CharField(max_length=3)),
                ('DataIngresso', models.DateField()),
                ('CargaHorariaSemanal', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ESPECIALIDADE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodEspec', models.CharField(max_length=3)),
                ('NomeEspec', models.CharField(max_length=130)),
                ('Descricao', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='MEDICO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodMed', models.CharField(max_length=3)),
                ('NomeMed', models.CharField(max_length=130)),
                ('Genero', models.CharField(max_length=1)),
                ('Telefone', models.CharField(max_length=11)),
                ('Email', models.CharField(max_length=130)),
                ('CodEspec', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='PACIENTE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CpfPaciente', models.CharField(max_length=11)),
                ('NomePac', models.CharField(max_length=130)),
                ('DataNascimento', models.DateField()),
                ('Genero', models.CharField(max_length=1)),
                ('Telefone', models.CharField(max_length=11)),
                ('Email', models.CharField(max_length=130)),
            ],
        ),
    ]
