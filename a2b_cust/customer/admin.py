from django.contrib import admin
from a2b_cust.customer.models import *
from django.contrib.sites.models import Site
#from django.contrib.admin.views.main import ChangeList

# Language
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','lname','charset')
    list_display_links = ('name',)
    #list_editable = ('code','charset')
    list_filter = ['charset']
    """
    def changelist_view(self, request, extra_context=None, **kwargs):
        cl = ChangeList(request, self.model, list(self.list_display),
                        self.list_display_links, self.list_filter,
                        self.date_hierarchy, self.search_fields,
                        self.list_select_related, self.list_per_page,
                        self.list_editable, self)
        cl.formset = None
        if extra_context is None:
            extra_context = {}
        if kwargs.get('only_tagged'):
            tag = kwargs.get('tag')
            cl.result_list = cl.result_list.filter(tags__icontains=tag)
            extra_context['extra_filter'] = "Only tagged %s" % tag

        extra_context['cl'] = cl
        return super(LanguageAdmin, self).changelist_view(request, extra_context=extra_context)
      """
admin.site.register(Language, LanguageAdmin)
admin.site.unregister(Site)

class CardAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            
            'fields': ('username', 'useralias','uipass','credit','id_group', 'serial','lastname','firstname',
                       'email','address','city','state','country','zipcode','phone','fax','company_name',
                       'company_website','typepaid','tariff','id_didgroup','id_timezone','currency','language',
                       'status','simultaccess','runservice','creditlimit','credit_notification','notify_email',
                       'email_notification','id_campaign','firstusedate','enableexpire','expirationdate',
                       'expiredays','sip_buddy','iax_buddy','mac_addr','inuse','autorefill','initialbalance',
                       'invoiceday','vat','vat_rn','discount','traffic','traffic_target','restriction')            
        }),
    )
    
    list_display = ('id', 'username', 'useralias','lastname','id_group','ba','tariff','status','language')
    list_display_links = ('username',)    
    search_fields = ('useralias', 'username')
    ordering = ('id',)
    list_filter = ['status','id_group','language']
    readonly_fields = ('username','credit','firstusedate')

admin.site.register(Card, CardAdmin)

class CallAdmin(admin.ModelAdmin):
    list_display = ('starttime','card_id', 'src', 'calledstation',  'sessiontime', 'real_sessiontime','terminatecauseid')
    list_display_links = []
    list_filter = ['starttime', 'calledstation']
    search_fields = ('card_id', 'dst', 'src','starttime',)
    ordering = ('-id',)
    
    def __init__(self, *args, **kwargs):
        super(CallAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = []

    


admin.site.register(Call, CallAdmin)