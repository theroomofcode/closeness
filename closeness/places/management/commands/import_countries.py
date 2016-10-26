# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import logging
import os
import shutil
import zipfile

import requests
from django.core.management import BaseCommand
from django.core.management import CommandError

from closeness.places.helpers import import_world_borders_shape_file

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Downloads and adds the Places models for countries.

    FIXME: Make sure that we always delete TM_WORLD_BORDERS-0.3.zip file and TM_WORLD_BORDERS folder
    after calling the handle method, even if there is an exception.
    """
    help = "Downloads and adds the Places models for countries"
    url = "http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip"
    filename = "TM_WORLD_BORDERS-0.3"
    extract_dir = "TM_WORLD_BORDERS"

    def handle(self, *args, **options):
        zip_filename = "%s.zip" % self.filename
        shp_filename = "%s.shp" % self.filename

        # Download file
        with open(zip_filename, 'wb') as handle:
            response = requests.get(self.url, stream=True)
            if not response.ok:
                raise CommandError("We couldn't download the world border file from %s" % self.url)
            for block in response.iter_content(1024):
                handle.write(block)

        # Unzip file
        with zipfile.ZipFile(zip_filename, "r") as zip_handle:
            zip_handle.extractall(self.extract_dir)
        os.remove(zip_filename)

        # Load shape file
        shape_file_path = os.path.join(self.extract_dir, shp_filename)
        import_world_borders_shape_file(shape_file_path)

        # Delete temporal files
        shutil.rmtree(self.extract_dir)
