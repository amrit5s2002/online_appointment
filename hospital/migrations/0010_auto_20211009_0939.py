# Generated by Django 3.2.4 on 2021-10-09 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_auto_20211008_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmenttime',
            field=models.TimeField(),
        ),
    ]