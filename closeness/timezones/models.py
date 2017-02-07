# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

from closeness.utils.models import GisTimeStampedModel


@python_2_unicode_compatible
class TimeZone(GisTimeStampedModel):
    """TimeZone GIS model, to obtain the timezone name using
    a point.
    """

    name = models.CharField(max_length=250)
    shape = models.GeometryField()

    def __str__(self):
        return self.name
