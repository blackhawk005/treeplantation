# Generated by Django 3.1.5 on 2021-07-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20210721_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='date',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='participants',
            name='time',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='pastevents',
            name='date',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='pastevents',
            name='time',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='tt',
            name='date',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='tt',
            name='time',
            field=models.CharField(max_length=300),
        ),
    ]