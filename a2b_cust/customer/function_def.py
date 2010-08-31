from a2b_cust.customer.models import *
from datetime import *
from random import *
import string
import calendar



def country_list():
        list = Country.objects.all()
        return ((l.countrycode, l.countryname) for l in list)


def get_unique_id():
    """get unique id"""
    length=8
    chars="abcdefghijklmnopqrstuvwxyz1234567890"
    return ''.join([choice(chars) for i in range(length)])


def pass_gen():
    char_length=2
    digit_length=6
    chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit="1234567890"
    pass_str_char = ''.join([choice(chars) for i in range(char_length)])
    pass_str_digit = ''.join([choice(digit) for i in range(digit_length)])
    return pass_str_char+pass_str_digit


def purchase_amount_str():
    purchase_amount_str = config_value('purchase_amount').replace(":","-")
    purchase_amount_str = purchase_amount_str + ' ' + config_value('base_currency').upper()
    return purchase_amount_str

def config_value(key):
    val = Config.objects.get(config_key=key)
    return val.config_value

def call_type_list():
    CALL_TYPE_LIST= ( (-1,'ALL CALLS'),(0,'STANDARD'),(1,'SIP/IAX'),(2,'DIDCALL'),(3,'DID_VOIP'),(4,'CALLBACK'),(5,'PREDICT'), )
    return CALL_TYPE_LIST


def dial_status_list():
    DIAL_STATUS_LIST= ( (1,'ANSWER'),(2,'BUSY'),(3,'NOANSWER'),(4,'CANCEL'),(5,'CONGESTION'),(6,'CHANUNAVAIL'),(7,'DONTCALL'),(8,'TORTURE'),(9,'INVALIDARGS'),)
    return DIAL_STATUS_LIST


def day_range():
    DAYS = range(1,32)
    days = map(lambda x:(x,x),DAYS)
    return days


def purchase_amount_list():
    purchase_amount_arr = config_value('purchase_amount').split(":")
    purchase_amount = map(lambda x:(x,x),purchase_amount_arr)
    return purchase_amount


def validate_days(year,month,day):
    total_days = calendar.monthrange(year,month)
    if day > total_days[1]:
        return total_days[1]
    else:
        return day


def month_year_range():
    tday = datetime.today()
    year_actual = tday.year
    YEARS = range(year_actual-1, year_actual+1)
    YEARS.reverse()
    m_list = []
    for n in YEARS:
        if year_actual == n:
            month_no = tday.month + 1
        else:
            month_no = 13
        months_list = range(1,month_no)
        months_list.reverse()
        for m in months_list:
            name = datetime(n, m,1).strftime("%B")
            str_year = datetime(n, m,1).strftime("%Y") 
            str_month = datetime(n, m,1).strftime("%m")
            sample_str = str_year+"-"+str_month
            sample_name_str = name + "-" + str_year
            m_list.append( (sample_str,sample_name_str) )
    return m_list


def currency_list():
    list = Currencies.objects.all()
    return ( (l.currency,l.name+"  -  ("+str(l.value)+")") for l in list)


def currency_value(currency_name):
    cur_row = Currencies.objects.get(currency=currency_name)
    return cur_row


def timezone_list():
    list = Timezone.objects.all()
    return ((l.id, l.gmtzone) for l in list)


#variable check with request
def variable_value(request,field_name):
    if request.method == 'GET':
        if field_name in request.GET:
            field_name = request.GET[field_name]
        else:
            field_name = ''

    if request.method == 'POST':
        if field_name in request.POST:
            field_name = request.POST[field_name]
        else:
            field_name = ''

    return field_name


#source_type/destination_type filed check with request
def source_desti_field_chk(base_field,base_field_type,field_name):
    kwargs = {}
    if base_field != '':
        if base_field_type == '1':
            kwargs[field_name + '__exact']      = base_field
        if base_field_type == '2':
            kwargs[field_name + '__startswith'] = base_field
        if base_field_type == '3':
            kwargs[field_name + '__contains']   = base_field
        if base_field_type == '4':
            kwargs[field_name + '__endswith']   = base_field
    return kwargs


#function create to test UnitTest    
def my_func(a_list, idx):
    """
    >>> a = ['larry', 'curly', 'moe']
    >>> my_func(a, 0)
    'larry'
    >>> my_func(a, 1)
    'curly'
    """
    return a_list[idx]


