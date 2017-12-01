# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from urlsite.models import Urls

# Register your models here.
class UrlsAdmin(admin.ModelAdmin):
	list_display = ('short_id', 'long_url')

admin.site.register(Urls, UrlsAdmin)