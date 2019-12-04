# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Calate(models.Model):
    a = models.FloatField(max_length=10)
    b = models.FloatField(max_length=10)
    result = models.FloatField(max_length=10)