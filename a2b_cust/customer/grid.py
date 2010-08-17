from customer.models import *
from jqgrid import *
from customer.views import *
from django.utils.translation import gettext as _


class ExampleGrid(JqGrid):
    model = Call # could also be a queryset
    queryset = Call.objects.values('starttime','card_id', 'calledstation','destination', 'real_sessiontime','sipiax','buycost').all()#filter(duration='30')
    fields = ['starttime','card_id', 'calledstation','destination', 'real_sessiontime','sipiax','buycost'] # optional
    caption = _('Call Detail Records') # optional
    colmodel_overrides = {
        'starttime'       :{ 'label' : _('Date'), 'width':50 },
        'card_id'         :{ 'label' : _('CallerID'), 'width':50  },
        'calledstation'   :{ 'label' : _('PhoneNumber'), 'width':50  },
        'destination'     :{ 'label' : _('Destination'), 'width':50  },
        'real_sessiontime':{ 'label' : _('Duration'), 'width':50 },
        'sipiax'          :{ 'label' : _('CallType'), 'width':50 },
        'buycost'         :{ 'label' : _('Cost'), 'width':50  },
    }
