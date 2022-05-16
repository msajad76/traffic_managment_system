from django.contrib import admin
from .models import Owner, Vehicle, Road, TollStation, Node
# Register your models here.

admin.site.register(Owner)
admin.site.register(Vehicle)
admin.site.register(Road)
admin.site.register(TollStation)
admin.site.register(Node)



