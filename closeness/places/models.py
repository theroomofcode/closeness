# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from django.contrib.gis.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Place(models.Model):
    """A 'Place' represents an area in the world with a name. It could be a country, a city, a
    neighborhood or any other kind of place.
    """
    name = models.CharField(max_length=250)
    shape = models.GeometryField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
