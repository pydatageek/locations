from django.views.generic import TemplateView

from .models import Country, City


class HomeView(TemplateView):
    template_name = 'home.html'


class CountryList(TemplateView):
    template_name = 'locations/country_list.html'


class CountryDetail(TemplateView):
    template_name = 'locations/country_detail.html'


class CountryEdit(TemplateView):
    template_name = 'locations/country_edit.html'


class CountryCreate(TemplateView):
    template_name = 'locations/country_create.html'


class CityList(TemplateView):
    template_name = 'locations/city_list.html'


class CityDetail(TemplateView):
    template_name = 'locations/city_detail.html'


class CityEdit(TemplateView):
    template_name = 'locations/city_edit.html'


class CityCreate(TemplateView):
    template_name = 'locations/city_create.html'
