from rest_framework import viewsets

from locations.models import Country, City
from .serializers import CountrySerializer, CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.prefetch_related('cities')
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.select_related('country')
    serializer_class = CitySerializer
