import os
from a2b_cust.customer.views import *
from django.conf import settings
from django.conf.urls.defaults import *
from a2b_cust.settings import *
from django_restapi.model_resource import * #Collection
from django_restapi.authentication import *
from django_restapi.responder import * #XMLResponder
from django_restapi.receiver import *
from a2b_cust.customer.forms import *
#site_media = os.path.join(os.path.dirname(__file__), 'site_media')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


def digest_authfunc(username, realm):
    #Exemplary authfunc for HTTP Digest. In production situations,
    #the combined hashes of realm, username and password are usually
    #stored in an external file/db.
    hashes = {
        ('realm1', 'john') : '3014aff1d0d0f0038e23c1195301def3', # Password: johnspass
        ('realm2', 'jim') : '5bae77fe607e161b831c8f8026a2ceb2'   # Password: jimspass
    }
    return hashes[(username, realm)]


language_xml_resource = Collection(
    queryset = Language.objects.all(),    
    permitted_methods = ('GET', 'POST', 'PUT', 'DELETE'),
    expose_fields = ('code', 'name','lname' ,'charset'),
    receiver = XMLReceiver(),
    #responder = XMLResponder(),
    responder = XMLResponder(paginate_by = 2),
    #authentication = HttpBasicAuthentication(),
    authentication = HttpDigestAuthentication(digest_authfunc, 'realm1'),
)

language_json_resource = Collection(
    queryset = Language.objects.all(),
    permitted_methods = ('GET', 'POST', 'PUT', 'DELETE'),
    receiver = JSONReceiver(),
    responder = JSONResponder()
)

language_template_resource = Collection(
    queryset = Language.objects.all(),
    permitted_methods = ('GET', 'POST', 'PUT', 'DELETE'),
    expose_fields = ('code', 'name','lname' ,'charset'),
    responder = TemplateResponder(
        template_dir = os.path.join( APPLICATION_DIR, 'templates' ),
        template_object_name = 'language',
        paginate_by = 10,
    ),
)



urlpatterns = patterns('',
    # redirect
    #('^$', 'django.views.generic.simple.redirect_to', {'url': '/'}),

    #(r'^/', include('a2b_cust.urls')),

    #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
    (r'^resources/(?P<path>.*)$',  'django.views.static.serve',{ 'document_root': settings.MEDIA_ROOT } ),

     # Jqgrid

    #url (r'^examplegrid/$', grid_handler, name='grid_handler'),
	#url (r'^examplegrid/cfg/$', grid_config, name='grid_config'),

	
    
    #To set the correct notify_url
    (r'^checkout_ipn_process/', include('paypal.standard.ipn.urls')),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    (r'^admin/(.*)', admin.site.root),

    url(r'^xml/language/(.*?)/?$', language_xml_resource),
    url(r'^json/language/(.*?)/?$', language_json_resource),

    url(r'^html/language/creator/$', language_template_resource.responder.create_form),
    url(r'^html/language/(?P<pk>\d+)/editor/$', language_template_resource.responder.update_form),
    url(r'^html/language/(.*?)/?$', language_template_resource),


)
urlpatterns += patterns('a2b_cust.customer.views',
    (r'^$', 'index_view'),
    (r'^login/$', 'check_login'),
    (r'^logout/$', 'logout_view'),
    (r'^profile/$', 'profile_view'),
    (r'^cdr/$', 'call_detail'),
    (r'^checkout_payment/$', 'checkout_payment'),
    (r'^checkout_confirmation/$', 'checkout_confirmation'),
    (r'^checkout_process/$', 'checkout_process'),
     # Jqgrid
    url (r'^examplegrid/$', grid_handler, name='grid_handler'),
    url (r'^examplegrid/cfg/$', grid_config, name='grid_config'),
)


