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
                rc.BAD_REQUEST
        else:
            return base.all()
    #curl -X GET http://127.0.0.1:8000/api/language
    #curl -X GET http://127.0.0.1:8000/api/language/xx/

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
    #curl -X  POST http://127.0.0.1:8000/api/language -d "code=xx&name=xxxxx&lname=xxxxx&charset=utf-8"


    #@throttle(5, 10*60) # allow 5 times in 10 minutes
    def update(self, request, code):
        #post = Language.objects.get(code=code)
        try :
            language = Language.objects.get(code=code)
            language.name = request.PUT.get('name')
            language.save()
            return language
        except :
            return rc.NOT_HERE
    #curl -X PUT http://127.0.0.1:8000/api/language/xx/ -d "name=xxxxx"

    def delete(self, request, code):
        #post = Blogpost.objects.get(slug=post_slug)
        try :
            language = Language.objects.get(code=code)
            language.delete()
            return rc.DELETED # returns HTTP 204
        except :
            return rc.NOT_HERE        
    #curl -X DELETE http://127.0.0.1:8000/api/language/xx/
    
    
class AnonymousLanguageHandler(LanguageHandler, AnonymousBaseHandler):
    """
    Anonymous entrypoint for language.
    """
    fields = ('lname')
