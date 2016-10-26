# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import json

import shapefile
from django.contrib.gis.geos import GEOSGeometry
from django.utils.encoding import force_text

from closeness.places.models import Place


def import_world_borders_shape_file(shape_file_path):
    """Given the path of the .shp file for the world borders, imports all
    countries as Places.

    Note: This works with http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip file.
    """
    sf = shapefile.Reader(shape_file_path)
    shape_records = sf.shapeRecords()
    for shape_record in shape_records:
        geometry = GEOSGeometry(json.dumps(shape_record.shape.__geo_interface__))
        fips, iso2, iso3, un, name, area, pop2005, region, subregion, lon, lat = shape_record.record
        name = force_text(name, errors="replace")
        Place.objects.update_or_create(
            name=name,
            defaults={
                "name": name,
                "shape": geometry
            }
        )
