# Generated by Django 4.1.5 on 2023-02-04 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profession',
        ),
    ]
