"""It is needed for bulk import from excel or csv"""
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Country, City


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country


class CityResource(resources.ModelResource):
    country = fields.Field(
        column_name='country',
        attribute='country',
        widget=ForeignKeyWidget(Country, 'name'))

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('country')

    class Meta:
        model = City
