# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from django.contrib.gis import admin

from closeness.places.models import Place


@admin.register(Place)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "order"]
    search_fields = ["name"]
