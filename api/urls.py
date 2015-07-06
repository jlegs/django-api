from django.conf.urls import patterns, url
from api.views import fizzbuzz


urlpatterns = patterns('',
	url(r'^', 'api.views.fizzbuzz', name='api'),
)