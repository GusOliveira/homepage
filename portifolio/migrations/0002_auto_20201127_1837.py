# Generated by Django 2.2.5 on 2020-11-27 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tittle',
            new_name='title',
        ),
    ]
