from django.contrib import admin

from commune.models import Commune


class CommuneAdmin(admin.ModelAdmin):
    list_display = ['nom', 'id', 'insee']
    search_fields = ['nom', 'id', 'insee', 'geom']


admin.site.register(Commune, CommuneAdmin)
