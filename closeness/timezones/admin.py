# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from django.contrib.gis import admin

from closeness.timezones.models import TimeZone


@admin.register(TimeZone)
class TimeZoneAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
