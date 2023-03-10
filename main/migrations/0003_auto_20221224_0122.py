# Generated by Django 3.2.16 on 2022-12-23 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=20, verbose_name='emotion')),
                ('imagename', models.CharField(max_length=20, verbose_name='imagename')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='calculations',
            field=models.IntegerField(default=0, verbose_name='calculations'),
        ),
    ]
