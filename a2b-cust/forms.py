from django import forms
from django.forms import ModelForm
from django.contrib import *
from mysite2.models import Country, Timezone, Card, Call

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)

def country_list():
    list = Country.objects.all()
    return ((l.countrycode, l.countryname) for l in list)

def timezone_list():
    list = Timezone.objects.all()
    return ((l.id, l.gmtzone) for l in list)

class CardForm(ModelForm):
    country  = forms.ChoiceField(choices=country_list())
    id_timezone = forms.ChoiceField(choices=timezone_list(),label='Timezone')
    class Meta:
        model = Card
        fields = ['lastname', 'firstname', 'address','city','state','country','zipcode','id_timezone','phone','fax']

