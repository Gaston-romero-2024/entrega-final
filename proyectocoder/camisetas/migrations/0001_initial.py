# Generated by Django 5.1.4 on 2024-12-20 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('titular', models.BooleanField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
