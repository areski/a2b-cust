import os

from django.conf import settings
from django.conf.urls.defaults import *
from agents import views

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
      (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
    
    #To set the correct notify_url
      (r'^checkout_ipn_process/', include('paypal.standard.ipn.urls')),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('agents.views',
   #(r'^login/$', 'check_login'),
    (r'^$', 'check_login'),
    (r'^logout/$', 'logout_view'),
    (r'^profile/$', 'profile_view'),
    (r'^cdr/$', 'call_detail'),
    (r'^checkout_payment/$', 'checkout_payment'),
    (r'^checkout_confirmation/$', 'checkout_confirmation'),
    (r'^checkout_process/$', 'checkout_process'),
)

