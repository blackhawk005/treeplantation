# Generated by Django 3.1.5 on 2021-07-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('unique_id', models.CharField(max_length=300)),
                ('event_name', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=300)),
                ('time', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='pastevents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('time', models.CharField(max_length=300)),
                ('host', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=300)),
                ('unique_id', models.CharField(max_length=300)),
                ('event_name', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('time', models.CharField(max_length=300)),
                ('host', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=300)),
                ('unique_id', models.CharField(max_length=300)),
                ('event_name', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=100)),
                ('reported', models.CharField(max_length=100)),
            ],
        ),
    ]
