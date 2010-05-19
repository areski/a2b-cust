from django import forms
from django.forms import ModelForm
from function_def import *
from django.contrib import *
from django import *
from django.contrib.admin.widgets import *

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)

class CardForm(ModelForm):
    country  = forms.ChoiceField(choices=country_list())
    id_timezone = forms.ChoiceField(choices=timezone_list(),label='Timezone')
    class Meta:
        model = Card
        fields = ['lastname', 'firstname', 'address','city','state','country','zipcode','id_timezone','phone','fax']

class SearchForm(forms.Form):
    fromday_chk = forms.BooleanField(label=u"DATE",required=False)
    from_day = forms.ChoiceField(label=u'From',choices=day_range())
    from_month_year= forms.ChoiceField(label=u'',choices=month_year_range())
    today_chk = forms.BooleanField(label="",required=True)
    to_day = forms.ChoiceField(label=u'To',choices=day_range())
    to_month_year = forms.ChoiceField(label=u'',choices=month_year_range())
    phone_no = forms.CharField(label=u'PHONENUMBER',widget=forms.TextInput(attrs={'size': 15}))
    phone_no_type = forms.TypedChoiceField(coerce=bool,choices=((1, 'Exact'), (2, 'Begins with'), (3, 'Contains'), (4, 'Ends with')),widget=forms.RadioSelect)    
    call_type = forms.ChoiceField(label=u'CALL TYPE',choices=call_type_list())
    show = forms.TypedChoiceField(label=u'Show:',coerce=bool,choices=(('ANSWER', 'Answered Calls'), ('ALL', 'All Calls')),widget=forms.RadioSelect)
    result = forms.TypedChoiceField(label=u'Result:',coerce=bool,choices=(('min', 'Minutes'), ('sec', 'Seconds')),widget=forms.RadioSelect)
    currency  = forms.ChoiceField(label=u'Currecny:',choices=currency_list())

class CheckoutPaymentForm(forms.Form):
    payment_method = forms.TypedChoiceField(coerce=bool,choices=(('paypal', 'PayPal'), ),widget=forms.RadioSelect)#('moneybookers','Moneybookers.com'), ('plugnpay', 'PlugnPay')
    purchase_amount = forms.ChoiceField(label=u'Total Amount:',choices=purchase_amount_list())

