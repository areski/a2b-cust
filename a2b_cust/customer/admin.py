from django.contrib import admin
from a2b_cust.customer.models import Agent, Card #Publisher, Author, Book

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'datecreation', 'login','passwd','firstname','lastname','credit','commission','currency','active')
    search_fields = ('id', 'login')

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'useralias','uipass','lastname','id_didgroup','status')
    search_fields = ('useralias', 'username')

#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'publisher', 'publication_date')
#    list_filter = ('publication_date',)
#    date_hierarchy = 'publication_date'
#    ordering = ('-publication_date',)
#    filter_horizontal = ('authors',)
#    raw_id_fields = ('publisher',)
#    fields = ('title', 'authors', 'publisher', 'publication_date')
#    search_fields = ('title', 'publisher')


admin.site.register(Agent, AgentAdmin)
admin.site.register(Card, CardAdmin)
#admin.site.register(Book, BookAdmin)

