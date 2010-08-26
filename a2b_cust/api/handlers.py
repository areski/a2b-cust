from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.emitters import *
from piston.utils import rc, require_mime, require_extended
from a2b_cust.customer.models import Language


class LanguageHandler(BaseHandler):
    model = Language
    allowed_methods = ('GET','POST','PUT', 'DELETE')
    anonymous = 'AnonymousLanguageHandler'
    fields = ('code', 'name', 'lname', 'charset')

    @classmethod
    def content_length(cls, language):
        return len(language.content)

    @classmethod
    def resource_uri(cls, language):
        return ('languages', [ 'json', ])

    def read(self, request, code=None):
        base = Language.objects
        if code :
            try :
                language = base.get(code=code)
                return language
            except :
                print "koko"
                rc.BAD_REQUEST
        else:
            return base.all()

    def create(self, request):
        attrs = self.flatten_dict(request.POST)
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            language = Language(code=attrs['code'],
                            name=attrs['name'],
                            lname=attrs['lname'],
                            charset=attrs['charset'] )
            language.save()
            return language
    
    
    #@throttle(5, 10*60) # allow 5 times in 10 minutes
    def update(self, request, code):
        try :
            language = Language.objects.get(code=code)
            language.name = request.PUT.get('name')
            language.save()
            return language
        except :
            return rc.NOT_HERE
            

    def delete(self, request, code):
        try :
            language = Language.objects.get(code=code)
            language.delete()
            return rc.DELETED # returns HTTP 204
        except :
            return rc.NOT_HERE
    
    
class AnonymousLanguageHandler(LanguageHandler, AnonymousBaseHandler):
    """
    Anonymous entrypoint for language.
    """
    fields = ('lname')
