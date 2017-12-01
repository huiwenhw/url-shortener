# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Urls(models.Model):
	short_id = models.SlugField(max_length=6,primary_key=True)
	long_url = models.URLField(max_length=200)

def __str__(self):
	return self.long_url