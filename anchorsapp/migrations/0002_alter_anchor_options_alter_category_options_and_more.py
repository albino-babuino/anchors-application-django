# Generated by Django 5.1.2 on 2024-10-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anchorsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anchor',
            options={'verbose_name': 'Enlace', 'verbose_name_plural': 'Enlaces'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AddField(
            model_name='category',
            name='bg_color',
            field=models.CharField(default='#1461f6', max_length=50, verbose_name='Color de fondo'),
        ),
    ]
