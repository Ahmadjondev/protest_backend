# Generated by Django 4.1.5 on 2023-02-02 16:18

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('science_id', models.IntegerField()),
                ('subject', models.TextField(verbose_name='Mavzu')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('science_id', models.IntegerField()),
                ('question_name', models.TextField(verbose_name='Savol')),
                ('question_image', models.ImageField(blank=True, null=True, upload_to=quiz.models.Quiz.nameFile, verbose_name='Subject Image:')),
                ('var_a_name', models.CharField(max_length=555, verbose_name='A:')),
                ('var_a_id', models.IntegerField()),
                ('var_b_name', models.CharField(max_length=555, verbose_name='B:')),
                ('var_b_id', models.IntegerField()),
                ('var_c_name', models.CharField(blank=True, max_length=555, verbose_name='C:')),
                ('var_c_id', models.IntegerField(blank=True)),
                ('var_d_name', models.CharField(blank=True, max_length=555, verbose_name='D:')),
                ('var_d_id', models.IntegerField(blank=True)),
                ('correct', models.IntegerField()),
            ],
        ),
    ]
