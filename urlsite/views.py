# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from urlsite.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.views import generic


# Create your views here.
class HomeView(generic.TemplateView):
	template_name = 'urlsite/home.html'
 
 # redirect if long url is found
def redirect_long(short_id):
	url = get_object_or_404(Urls, pk=short_id) 
	return HttpResponseRedirect(url.long_url)
 
def short_url(request):
	if request.POST:
		url = request.POST['shorturl']
		length = 6
		char = string.ascii_uppercase + string.digits + string.ascii_lowercase
		short_id = ''
		while True:
			short_id = ''.join(random.choice(char) for x in range(length))
			try:
				temp = Urls.objects.get(pk=short_id)
			except:
				break
		saveurl = Urls(long_url=url, short_id=short_id)
		saveurl.save()
		
		# return shortened url as a id
		return render(request, 'urlsite/home.html', {'msg':short_id})
	return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")