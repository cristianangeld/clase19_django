# Generated by Django 4.2.1 on 2023-05-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_estudios', '0002_alter_entregable_fecha_entrega_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='cursos',
            field=models.ManyToManyField(to='control_estudios.curso'),
        ),
    ]
