from piston.handler import BaseHandler
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
        """
        Reads all languages, or a specific language if
        `code` is supplied.
        
        Attributes : 
        [code value]
        
        CURL Testing :
        curl -u username:password -i -H "Accept: application/json" -X GET http://127.0.0.1:8000/api/language
        curl -u username:password -i -H "Accept: application/json" -X GET http://127.0.0.1:8000/api/language/xx/
        """
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
        """
        Create new language
        
        Attributes : 
        code, name, lname, charset
        
        CURL Testing :
        curl -u username:password -i -H "Accept: application/json" -X POST http://127.0.0.1:8000/api/language -d "code=br&name=brazil&lname=brazil&charset=utf-8"
        """
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
        """
        Update language
        
        Attributes : 
        code, name, lname, charset
        
        CURL Testing :
        curl -u username:password -i -H "Accept: application/json" -X PUT http://127.0.0.1:8000/api/language/br/ -d "name=Brazilian"
        """
        try :
            language = Language.objects.get(code=code)
            language.name = request.PUT.get('name')
            language.save()
            return language
        except :
            return rc.NOT_HERE
            

    def delete(self, request, code):
        """
        Delete language
        
        CURL Testing :
        curl -u username:password -i -H "Accept: application/json" -X DELETE http://127.0.0.1:8000/api/language/br/
        """
        try :
            language = Language.objects.get(code=code)
            language.delete()
            return rc.DELETED # returns HTTP 204
        except :
            return rc.NOT_HERE




"""
# Generate Doc
doc_list = [LanguageHandler]
for doc_elem in doc_list:
    doc = generate_doc(doc_elem)
    print "=========================================================================================================="
    print "API : " + doc.name # -> 'LanguageHandler'
    #print doc.model # -> <class 'Language'>
    #print doc.resource_uri_template # -> '/api/post/{id}'
    methods = doc.get_methods()

    for method in methods:
        print ""
        print "-------------------------------------------------"
        print "METHOD : " + method.name # -> 'read'
        if len(method.signature) > 0 :
            print "SIGNATURE : " + method.signature # -> 'read(post_slug=<optional>)'
        print ""
        print method.doc   
        sig = ''
        for argn, argdef in method.iter_args():
            sig += argn
            if argdef:
                sig += "=%s" % argdef
            sig += ', '

        sig = sig.rstrip(",")
        #print "url attribute:" + sig # -> 'read(repo_slug=None)'
"""
