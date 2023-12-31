# Generated by Django 4.2.1 on 2023-09-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('date_presence', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
