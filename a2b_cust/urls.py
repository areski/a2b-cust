import os
from a2b_cust.customer.views import *
from a2b_cust.customer.forms import *
from a2b_cust.customer.models import Language

from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # redirect
    #('^$', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    #(r'^/', include('a2b_cust.urls')),
    (r'^resources/(?P<path>.*)$',  'django.views.static.serve',{ 'document_root': settings.MEDIA_ROOT } ),

    #To set the correct paypal notify_url
    (r'^checkout_ipn_process/', include('paypal.standard.ipn.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/language/$', 'a2b_cust.customer.views.my_admin_language_view'),
    (r'^admin/card/$', 'a2b_cust.customer.views.my_admin_card_view'),
    (r'^admin/cdr/$', 'a2b_cust.customer.views.my_admin_cdr_view'),
    (r'^admin/(.*)', admin.site.root),

    (r'^api/', include('a2b_cust.api.urls')),
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



