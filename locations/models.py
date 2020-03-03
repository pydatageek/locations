from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    iso2 = models.CharField(max_length=2, unique=True)

    def get_absolute_url(self):
        return reverse('country_detail', args=[self.pk])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('name',)


class City(models.Model):
    name = models.CharField(max_length=75)
    cid = models.IntegerField(unique=True)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='cities')

    def get_absolute_url(self):
        return reverse('city_detail', args=[self.pk])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
        unique_together = ('name', 'latitude', 'longitude')
        ordering = ('country', 'name')
