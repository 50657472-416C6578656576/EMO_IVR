# Generated by Django 3.1.3 on 2021-01-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210128_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='preview',
            field=models.ImageField(default='pictures/default.jpg', upload_to='pictures/', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='full_text',
            field=models.TextField(default='...', max_length=5000, verbose_name='Описание'),
        ),
    ]
