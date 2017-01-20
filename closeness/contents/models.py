# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel


class Tag(TimeStampedModel):
    """Simple tag."""
    name = models.CharField(max_length=140, unique=True, db_index=True)


class Content(TimeStampedModel, models.Model):
    """Generic content, with coordinates."""

    title = models.TextField(max_length=140)
    body = models.TextField()
    position = models.PointField()

    places = models.ManyToManyField("places.Place", blank=True, related_name="contents")
    tags = models.ManyToManyField("contents.Tag", blank=True, related_name="contents")
