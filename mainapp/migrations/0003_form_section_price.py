# Generated by Django 2.0.2 on 2018-10-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_form_section_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_section',
            name='price',
            field=models.IntegerField(default=50),
        ),
    ]
