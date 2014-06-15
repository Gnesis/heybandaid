from django.shortcuts import render
from django.http import HttpResponse

from concerts.models import Concert
from artists.models import Artist

from pprint import pprint

import json

# Create your views here.

def get_concerts( request ):
	concerts_array = []
	try:
		concerts = Concert.objects.all().order_by('created')
		for concert in concerts:
			description = concert.description
			concerts_array.append( { 'slug': concert.slug, 'name': concert.name, 'poster': str(concert.poster), 'budget': concert.budget, 'place': concert.place, 'date': concert.date.strftime('%d/%m/%Y'), 'description': str(description.rendered) } )
	except:
		context = { 'error': 'error', 'msg': 'you can\'t always get what you want' }
	return HttpResponse( json.dumps( concerts_array ), content_type="application/json" )

def get_artists( request ):
	try:
		concerts = Concert.objects.all().filter().order_by('created')
	except:
		context = { 'error': 'error', 'msg': 'you can\'t always get what you want' }
	return HttpResponse( json.dumps( concerts ), content_type="application/json" )