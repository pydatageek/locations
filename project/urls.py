from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from locations.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', include('locations.urls')),
    path('', HomeView.as_view(), name='home'),

    # rest framework api urls
    # rest_framework login/logout
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include('locations.api.urls')),
]

# debug_toolbar for debug=True
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
