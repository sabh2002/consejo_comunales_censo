# Generated by Django 4.2.6 on 2023-11-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('censo', '0002_alter_jefefamiliar_numerocalle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitante',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Primer Apellido'),
        ),
        migrations.AlterField(
            model_name='habitante',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Primer Nombre'),
        ),
    ]
