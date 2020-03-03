from django.views.generic import TemplateView

from .models import Country, City


class HomeView(TemplateView):
    template_name = 'home.html'


class CountryList(TemplateView):
    template_name = 'locations/country_list.html'


class CountryDetail(TemplateView):
    template_name = 'locations/country_detail.html'


class CityList(TemplateView):
    template_name = 'locations/city_list.html'


class CityDetail(TemplateView):
    template_name = 'locations/city_detail.html'
