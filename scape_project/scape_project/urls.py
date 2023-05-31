from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

appname = 'Scape'
schema_view = get_schema_view(
    openapi.Info(
        title="Scape API Documentation",
        default_version='v1',
        description="description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@scape.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Auth url
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),

    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ADMIN URL
    path('', RedirectView.as_view(url='/admin')),
    path('admin/', admin.site.urls),

    # Commune URL
    path('', include('commune.urls')),
    path('', include('shapefile_data.urls'))
]
