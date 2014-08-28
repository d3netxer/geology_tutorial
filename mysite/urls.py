from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
    TemplateView.as_view(template_name='units/nearby.html'),
    name='near-me'),
    url(r'^find/$', 'units.views.find_rocks', name='find-rocks'),
)
