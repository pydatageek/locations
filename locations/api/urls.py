from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, CityViewSet

router = DefaultRouter()
router.register('country', CountryViewSet)
router.register('city', CityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
