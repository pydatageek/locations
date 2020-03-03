from rest_framework import serializers

from locations.models import Country, City


class CountrySerializer(serializers.ModelSerializer):
    # cities = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ('id', 'name', 'iso2', 'cities')

    # def get_cities(self, obj):
    #     return obj.cities


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ('id', 'name', 'cid', 'latitude',
                  'longitude', 'country', 'country_name')

    def get_country_name(self, obj):
        return obj.country.name
