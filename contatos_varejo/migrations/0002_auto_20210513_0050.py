# Generated by Django 3.2.2 on 2021-05-13 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos_varejo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contatovarejo',
            old_name='celular',
            new_name='cellphone',
        ),
        migrations.RenameField(
            model_name='contatovarejo',
            old_name='nome',
            new_name='name',
        ),
    ]