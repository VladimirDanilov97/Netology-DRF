# Generated by Django 4.0.1 on 2022-06-24 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_data_alter_measurement_sensor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 10, 21, 20, 451441)),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
