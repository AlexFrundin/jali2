# Generated by Django 2.0.2 on 2018-10-03 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_section',
            name='price',
        ),
    ]