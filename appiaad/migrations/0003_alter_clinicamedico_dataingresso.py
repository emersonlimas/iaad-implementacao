# Generated by Django 3.2.9 on 2021-11-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appiaad', '0002_auto_20211129_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicamedico',
            name='dataingresso',
            field=models.CharField(max_length=300),
        ),
    ]
