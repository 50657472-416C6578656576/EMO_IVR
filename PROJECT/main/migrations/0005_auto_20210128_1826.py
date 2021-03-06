# Generated by Django 3.1.3 on 2021-01-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210128_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsman',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='full_text',
            field=models.TextField(default='...', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='about',
            field=models.CharField(default='...', max_length=250, verbose_name='Характеристика'),
        ),
    ]
