# Generated by Django 3.2.16 on 2022-12-23 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20221224_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='imagename',
            field=models.CharField(max_length=200, verbose_name='imagename'),
        ),
    ]
