from django.conf.urls.defaults import *
from piston.resource import Resource
from a2b_cust.api.handlers import *

language_handler = Resource(LanguageHandler)

urlpatterns = patterns('',
   #url(r'^language/(?P<post_slug>[^/]+)/', language_handler),
   url(r'^language/(?P<code>[^/]+)/', language_handler),
   #url(r'^language/(?P<id>\d+)$', task_resource),
   url(r'^language$', language_handler),
)



