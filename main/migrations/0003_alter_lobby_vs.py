# Generated by Django 4.2.7 on 2024-01-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lobby_grid11_lobby_grid12_lobby_grid13_lobby_grid21_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='vs',
            field=models.CharField(default='', max_length=200),
        ),
    ]
