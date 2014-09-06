from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.gis.geos import Point
from djgeojson.serializers import Serializer as GeoJSONSerializer

# http://stackoverflow.com/questions/22511792/python-from-dotpackage-import-syntax
# explains the dot notation
from .models import Unit

def find_rocks(request):
	"""
	Give a lat/lon pair, return the unit(s) surround it.
	"""
	#if request.is_ajax():
	lat = request.GET.get('lat', None)
	lon = request.GET.get('lon', None)
    
	money = 'one_mil'
        
    #else: 
    	#msg = "Bad request: no AJAX present"
    	#return HttpResponseBadRequest(msg)
        
	
		
	#point = Point(float(lon), float(lat))
	lon = float(lon)
	lat = float(lat)
	point2 = Point(lon,lat)
	
	#return HttpResponse(lon)
	
	
	pnt = Point(-104.93, 39.73)
	
	units = Unit.objects.filter(geom__contains=point2)
	#geojson_data = GeoJSONSerializer().serialize(Unit.objects.all(), use_natural_keys=True) 
	
	print ('hello')
	
	#originally I tried .get() , but that returned a MultipleObjectsReturned error
	#so I changed it to .filter()
	results = Unit.objects.filter(name="Intrusion")
	
	
	geojson_data = GeoJSONSerializer().serialize(units, use_natural_keys=True) 
	
	'''
	if lat and lon:
		foo2 = "Hello, world. You're at %s." % lat
		return HttpResponse(foo2)
		#return HttpResponse("Hello, world. You're at nowhere.")
	'''
	
	return HttpResponse(geojson_data,content_type='application/json')
	
	#else:   
		#msg = "Bad request: no latlong pair present"
		#return HttpResponseBadRequest(msg)

	