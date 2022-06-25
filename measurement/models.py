from pyexpat import model
from django.db import models
from datetime import datetime


class Sensor(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f'{self.name}'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, related_name='measurements')
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, null=True, upload_to='media/')

    def __str__(self):
        return f'{self.sensor_id}: {self.temperature} {self.date}' 