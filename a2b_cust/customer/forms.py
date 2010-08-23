from django import *
from django import forms
from a2b_cust.customer.function_def import *
from django.forms import ModelForm
from django.contrib import *
from django.contrib.admin.widgets import *
from uni_form.helpers import *
from django.utils.translation import ugettext_lazy as _
from django import forms
#from django.shortcuts import render_to_response
#from datetime import *


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100,required=True,)
	password = forms.CharField(widget=forms.PasswordInput(),max_length=100,required=True,)
    
    
class CardForm(ModelForm):
    country  = forms.ChoiceField(choices=country_list())
    id_timezone = forms.ChoiceField(choices=timezone_list(),label='Timezone',required=True)
    class Meta:
        model = Card
        fields = ['lastname', 'firstname', 'address','city','state','country','zipcode','id_timezone','phone','fax']
        
class SearchForm(forms.Form):
    fromday_chk = forms.BooleanField(label=u'FROM :',required=False,)
    from_day = forms.ChoiceField(label=u'',choices=day_range(),required=False,)
    from_month_year= forms.ChoiceField(label=u'',choices=month_year_range(),required=False,)
    today_chk = forms.BooleanField(label='TO :',required=False,)
    to_day = forms.ChoiceField(label=u'',choices=day_range(),required=False,)
    to_month_year = forms.ChoiceField(label=u'',choices=month_year_range(),required=False,)
    phone_no = forms.CharField(label=u'PHONE NO :',widget=forms.TextInput(attrs={'size': 15}),required=False,)
    phone_no_type = forms.TypedChoiceField(coerce=bool,choices=((1, 'Exact'), (2, 'Begins with'), (3, 'Contains'), (4, 'Ends with')),widget=forms.RadioSelect,required=False,label=u'PHONE NO TYPE :',)
    call_type = forms.ChoiceField(label=u'CALL TYPE :',choices=call_type_list(),required=False,)
    show = forms.TypedChoiceField(label=u'SHOW :',coerce=bool,choices=(('ANSWER', 'Answered Calls'), ('ALL', 'All Calls')),widget=forms.RadioSelect,required=False,)
    result = forms.TypedChoiceField(label=u'RESULT :',coerce=bool,choices=(('min', 'Minutes'), ('sec', 'Seconds')),widget=forms.RadioSelect,required=False,)
    currency  = forms.ChoiceField(label=u'CURRENCY :',choices=currency_list(),required=False,)
    

class CheckoutPaymentForm(forms.Form):
    payment_method = forms.TypedChoiceField(coerce=bool,choices=(('paypal', 'PayPal'), ),widget=forms.RadioSelect)#('moneybookers', 'Moneybookers.com'), ('plugnpay', 'PlugnPay')
    purchase_amount = forms.ChoiceField(label=u'Total Amount:',choices=purchase_amount_list())