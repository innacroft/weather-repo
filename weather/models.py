from django.db import models

class City(models.Model):
    id_api=models.IntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    coord_lon = models.DecimalField(max_digits=10, decimal_places=10)
    coord_lat = models.DecimalField(max_digits=10, decimal_places=10)