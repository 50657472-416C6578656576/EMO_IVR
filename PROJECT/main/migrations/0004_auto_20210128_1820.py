# Generated by Django 3.1.3 on 2021-01-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='full_text',
            field=models.TextField(default='Пусто...', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='sportsman',
            name='about',
            field=models.CharField(default='Пусто...', max_length=250, verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='free_access',
            field=models.BooleanField(default=True, verbose_name='Доступно'),
        ),
    ]
