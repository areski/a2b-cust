from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
from a2b_cust.customer.models import Language




class LanguageHandler(BaseHandler):
    #allowed_methods = ('GET',)
    model = Language   
    #anonymous = 'AnonymousBlogpostHandler'
    fields = ('lname', 'code' )
    exclude = () # To display the ID

    @classmethod
    def content_length(cls, language):
        return len(language.content)
        
    def read1(self, request, code):
        #f = Language.objects.get(pk=1)
        try :
            f = Language.objects.get(code=code)
        except :
            f = 'a'
        return { 'language': f }


class AnonymousLanguageHandler(LanguageHandler, AnonymousBaseHandler):
    """
    Anonymous entrypoint for language.
    """
    fields = ('lname')
