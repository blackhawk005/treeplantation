# Generated by Django 3.1.5 on 2021-07-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20210721_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='participants',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='pastevents',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pastevents',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='tt',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tt',
            name='time',
            field=models.TimeField(),
        ),
    ]