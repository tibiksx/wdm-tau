# Generated by Django 3.0.4 on 2020-03-27 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tema3', '0009_label'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comm',
            new_name='Comment',
        ),
    ]