# Generated by Django 3.2.7 on 2021-10-16 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teste',
        ),
        migrations.AddField(
            model_name='customers',
            name='latitude',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='longitude',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customers',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=25),
        ),
        migrations.AlterField(
            model_name='customers',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]