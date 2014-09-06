from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import Unit

from units import views


urlpatterns = patterns('',
    url(r'^$', GeoJSONLayerView.as_view(model=Unit), name='units-json')
    url(r'^nearby/$',TemplateView.as_view(template_name='units/nearby.html'),name='near-me'),
    url(r'^nearby/find/$', 'units.views.find_rocks', name='find-rocks'),    
)
