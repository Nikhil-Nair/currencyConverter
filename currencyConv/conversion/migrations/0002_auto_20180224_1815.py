# Generated by Django 2.0.2 on 2018-02-24 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='values',
            old_name='currency',
            new_name='name',
        ),
    ]
