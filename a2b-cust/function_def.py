from models import *
from datetime import *
import calendar
from random import *
import string

def get_unique_id():
    """get unique id"""
    length=8
    chars="abcdefghijklmnopqrstuvwxyz1234567890"
    return ''.join([choice(chars) for i in range(length)])

def config_value(key):
    val = Config.objects.get(config_key=key)
    return val.config_value

def call_type_list():
    CALL_TYPE_LIST= ( (-1,'ALL CALLS'),(0,'STANDARD'),(1,'SIP/IAX'),(2,'DIDCALL'),(3,'DID_VOIP'),(4,'CALLBACK'),(5,'PREDICT'), )
    return CALL_TYPE_LIST

def dial_status_list():
    DIAL_STATUS_LIST= ( 
(1,'ANSWER'),(2,'BUSY'),(3,'NOANSWER'),(4,'CANCEL'),(5,'CONGESTION'),(6,'CHANUNAVAIL'),(7,'DONTCALL'),(8,'TORTURE'),(9,'INVALIDARGS'),)
    return DIAL_STATUS_LIST

def purchase_amount_list():
    purchase_amount_arr = config_value('purchase_amount').split(":")
    purchase_amount = map(lambda x:(x,x),purchase_amount_arr)
    return purchase_amount

def day_range():
    DAYS = range(1,32)
    days = map(lambda x:(x,x),DAYS)
    return days

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

def validate_days(year,month,day):
    total_days = calendar.monthrange(year,month)
    if day > total_days[1]:
        return total_days[1]
    else:
        return day

def country_list():
    list = Country.objects.all()
    return ((l.countrycode, l.countryname) for l in list)

def currency_list():
    list = Currencies.objects.all()
    return ( (l.currency,l.name+"  -  ("+str(l.value)+")") for l in list)

def currency_value(currency_name):
    cur_row = Currencies.objects.get(currency=currency_name)
    return cur_row

def timezone_list():
    list = Timezone.objects.all()
    return ((l.id, l.gmtzone) for l in list)
