# Generated by Django 4.2.16 on 2024-12-06 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_alter_antecedentespaciente_antecedente_descrip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentespaciente',
            name='antecedente_descrip',
            field=models.TextField(default='No aplica'),
        ),
    ]