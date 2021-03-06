# Generated by Django 3.2.4 on 2021-10-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20211005_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
    ]
