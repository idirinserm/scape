from django.contrib import admin

from shapefile_data.models import Shapefile


class ShapefileAdmin(admin.ModelAdmin):
    list_display = ["id", "ObjectName"]
    search_fields = ["id"]


admin.site.register(Shapefile, ShapefileAdmin)
