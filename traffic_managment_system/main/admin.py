from django.contrib import admin
from .models import Owner, Vehicle, Road, TollStation, Node
from django.contrib.gis import admin as gis_admin


admin.site.register(Vehicle)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


@gis_admin.register(TollStation)
class TollAdmin(gis_admin.GISModelAdmin):
    list_display = ['id', 'name', 'location', 'toll_per_cross']
    list_display_links = ['name']


@gis_admin.register(Node)
class NodeAdmin(gis_admin.GISModelAdmin):
    list_display = ['id', 'car', 'location', 'date']
    list_display_links = ['car']


@gis_admin.register(Road)
class RoadAdmin(gis_admin.GISModelAdmin):
    list_display = ['id', 'name', 'width', 'geom']
    list_display_links = ['name']
