# Generated by Django 5.0.6 on 2024-06-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['-created'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='precion',
            new_name='precio',
        ),
        migrations.AlterField(
            model_name='cursos',
            name='autor',
            field=models.TextField(),
        ),
    ]
