# Generated by Django 3.1.3 on 2021-01-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210128_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='participants',
            field=models.ManyToManyField(null=True, to='main.Sportsman'),
        ),
    ]