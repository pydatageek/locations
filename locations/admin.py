from django.contrib import admin
from django.db.models import Count

from import_export.admin import ImportExportModelAdmin

from .models import Country, City
from .resources import CountryResource, CityResource


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

    search_fields = ('name', 'iso2')

    list_display = ('name', 'iso2', 'get_cities_count')

    def get_queryset(self, request):
        """needed to be overriden for lesser queries"""
        qs = super().get_queryset(request)
        return qs.annotate(_cities_count=Count('cities', distinct=True))

    def get_cities_count(self, obj):
        return obj._cities_count
    get_cities_count.short_description = '# Cities'
    get_cities_count.admin_order_field = '_cities_count'


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource

    search_fields = ('name', 'country__name')

    list_display = ('cid', 'name', 'latitude', 'longitude', 'country')
    list_display_links = ('name',)
