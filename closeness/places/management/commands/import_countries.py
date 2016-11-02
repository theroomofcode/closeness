# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import json
import logging
import os
import zipfile

import requests
import shapefile
from django.contrib.gis.geos import GEOSGeometry
from django.core.management import BaseCommand
from django.core.management import CommandError
from django.utils.encoding import force_text

from closeness.utils.decorators import delete_after
from closeness.places.models import Place
from closeness.utils.management import ProgressBarCommand

logger = logging.getLogger(__name__)


class Command(ProgressBarCommand, BaseCommand):
    """Downloads and adds the Places models for countries."""
    help = "Downloads and adds the Places models for countries"
    url = "http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip"
    cache_dir = ".downloading"
    filename = "TM_WORLD_BORDERS-0.3"
    extract_dir = "TM_WORLD_BORDERS"

    @delete_after(cache_dir)
    def handle(self, *args, **options):
        # Files and download dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        zip_filename = os.path.join(self.cache_dir, "%s.zip" % self.filename)
        shp_filename = "%s.shp" % self.filename

        # Download file
        self.stdout.write(
            self.style.SUCCESS("Downloading {} file... ".format(zip_filename))
        )
        chunk_size = 1024
        with open(zip_filename, 'wb') as handle:
            response = requests.get(self.url, stream=True)
            file_size = int(response.headers["Content-Length"])
            if not response.ok:
                raise CommandError("We couldn't download the world border file from %s" % self.url)
            handle_size = 0
            for block in response.iter_content(chunk_size):
                handle.write(block)
                handle_size += chunk_size
                self.bar(handle_size / file_size)

        # Unzip file
        with zipfile.ZipFile(zip_filename, "r") as zip_handle:
            zip_handle.extractall(os.path.join(self.cache_dir, self.extract_dir))

        # Load shape file
        self.stdout.write('')
        self.stdout.write(
            self.style.SUCCESS("Indexing shapes... ")
        )
        shape_file_path = os.path.join(self.cache_dir, self.extract_dir, shp_filename)
        sf = shapefile.Reader(shape_file_path)
        shape_records = sf.shapeRecords()
        total_records = len(shape_records)
        counter_records = 0
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
            counter_records += 1
            self.bar(counter_records / total_records)
