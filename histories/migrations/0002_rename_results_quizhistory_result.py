# Generated by Django 4.1.6 on 2023-05-08 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizhistory',
            old_name='results',
            new_name='result',
        ),
    ]
