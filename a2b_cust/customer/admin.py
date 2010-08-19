from django.contrib import admin
from a2b_cust.customer.models import * #Publisher, Author, Book

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'datecreation', 'login','passwd','firstname','lastname','credit','commission','currency','active')
    search_fields = ('id', 'login')



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
    #fields = ('id', 'username', 'useralias','lastname','id_didgroup','status')
    search_fields = ('useralias', 'username')
    ordering = ('id',)
    readonly_fields = ('username','credit','firstusedate')


#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'publisher', 'publication_date')
#    list_filter = ('publication_date',)
#    date_hierarchy = 'publication_date'
#    ordering = ('-publication_date',)
#    filter_horizontal = ('authors',)
#    raw_id_fields = ('publisher',)
#    fields = ('title', 'authors', 'publisher', 'publication_date')
#    search_fields = ('title', 'publisher')


#admin.site.register(Agent, AgentAdmin)
admin.site.register(Card, CardAdmin)
#admin.site.register(Book, BookAdmin)

