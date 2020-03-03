from django.urls import path

from .views import (CountryList, CountryDetail, CityList, CityDetail)

urlpatterns = [
    path('country/', CountryList.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetail.as_view(), name='country_detail'),
    path('city/', CityList.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetail.as_view(), name='city_detail'),
]
