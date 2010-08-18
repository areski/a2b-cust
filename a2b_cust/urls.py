import os
from a2b_cust.customer.views import *
from django.conf import settings
from django.conf.urls.defaults import *


#site_media = os.path.join(os.path.dirname(__file__), 'site_media')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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


