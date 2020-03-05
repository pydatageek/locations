from django.urls import path

from .views import (
    CountryList, CountryDetail, CountryEdit, CountryCreate,
    CityList, CityDetail, CityEdit, CityCreate)

urlpatterns = [
    path('country/', CountryList.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetail.as_view(), name='country_detail'),
    path('country/<int:pk>/edit/', CountryEdit.as_view(), name='country_edit'),
    path('country/create/', CountryCreate.as_view(), name='country_create'),
    path('city/', CityList.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetail.as_view(), name='city_detail'),
    path('city/<int:pk>/edit/', CityEdit.as_view(), name='city_edit'),
    path('city/create/', CityCreate.as_view(), name='city_create'),
]
