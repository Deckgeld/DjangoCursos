# Generated by Django 5.0.6 on 2024-06-20 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_cursos_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['created'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
