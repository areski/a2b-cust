from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.doc import documentation_view
from a2b_cust.api.handlers import *
from piston.authentication import HttpBasicAuthentication, HttpBasicSimple

auth = HttpBasicAuthentication(realm='Language Application')

language_handler = Resource(LanguageHandler, authentication=auth)

urlpatterns = patterns('',
   #url(r'^language/(?P<post_slug>[^/]+)/', language_handler),
   url(r'^language/(?P<code>[^/]+)/', language_handler),
   #url(r'^language/(?P<id>\d+)$', task_resource),
   url(r'^language$', language_handler),

   # automated documentation
   url(r'^$', documentation_view),
)



