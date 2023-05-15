# Generated by Django 4.1.6 on 2023-05-08 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=500)),
                ('started_at', models.DateTimeField()),
                ('time', models.IntegerField(default=360)),
                ('contest_type', models.IntegerField(default=0)),
                ('code', models.CharField(blank=True, max_length=6, null=True)),
                ('ball', models.DecimalField(decimal_places=2, max_digits=3)),
                ('position_1', models.IntegerField(blank=True, default=0, null=True)),
                ('position_2', models.IntegerField(blank=True, default=0, null=True)),
                ('position_3', models.IntegerField(blank=True, default=0, null=True)),
                ('powered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
                ('questions', models.ManyToManyField(blank=True, to='quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='ContestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('ball', models.DecimalField(decimal_places=2, max_digits=3)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
