# Generated by Django 3.2.4 on 2021-06-29 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
