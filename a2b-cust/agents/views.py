from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import * #Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login ,logout
from django.contrib.sessions import *
from forms import *
from datetime import *
from django.core.paginator import *
from mysite2.models import Card, Tariffgroup, PackageOffer, Call, Config

#used to display SQL queries
from django.db import connection


ITEMS_PER_PAGE = 10

def call_type_list():
    CALL_TYPE_LIST= (
    (0,'STANDARD'),(1,'SIP/IAX'),(2,'DIDCALL'),(3,'DID_VOIP'),(4,'CALLBACK'),(5,'PREDICT'),
    )
    return CALL_TYPE_LIST

def dial_status_list():
    DIAL_STATUS_LIST= (
    (1,'ANSWER'),(2,'BUSY'),(3,'NOANSWER'),(4,'CANCEL'),(5,'CONGESTION'),(6,'CHANUNAVAIL'),(7,'DONTCALL'),(8,'TORTURE'),(9,'INVALIDARGS'),
    )
    return DIAL_STATUS_LIST

def config_value(key):
    val = Config.objects.get(config_key=key)
    return val


"""
view logic
"""
def call_detail(request):
    if request.method == 'GET' and "card_id" in request.session:
        card  = Card.objects.get(id=request.session.get("card_id"))
        tday = datetime.today()
        tday = datetime(2010, 3, 1, 13, 40, 53, 762759)
        calls = Call.objects.filter(card_id=request.session.get("card_id"),starttime__gte=datetime(tday.year, tday.month, 
tday.day)).order_by('-starttime')
        
        tariffgrp = Tariffgroup.objects.all()
        count = calls.count()
        #pre_fix = Prefix.objects.all()
        paginator = Paginator(calls, ITEMS_PER_PAGE)
        try:
            page_number = int(request.GET['page'])
        except (KeyError, ValueError):
            page_number = 1
        try:
            page = paginator.page(page_number)
        except InvalidPage:
            raise Http404
        calls = page.object_list
        
        print connection.queries
        
        variables = RequestContext(request,
                    {'calls':calls,
                     'count':count,
                     'base_currency':config_value('base_currency'),
                     'call_type':call_type_list(),
                     #'pre_fix':pre_fix,
                     'tariffgrp':tariffgrp,
                     'dial_status':dial_status_list(),
                     'card_id':card.id,
                     'title':'A2Billing | Call History',
                     'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
                     'content':'',
                     'show_paginator': paginator.num_pages > 1,
                     'has_prev': page.has_previous(),
                     'has_next': page.has_next(),
                     'page': page_number,
                     'pages': paginator.num_pages,
                     'next_page': page_number + 1,
                     'prev_page': page_number - 1
                     })
        return render_to_response('call_detail.html', variables)
    else:
        logout(request)
        return HttpResponseRedirect('/')

def profile_view(request):
    def errorHandle(error):
		form = CardForm()
		return render_to_response('profile_view.html', {'error' : error,'form' : form,	})
    errors = []
    if request.method == 'POST' and "card_id" in request.session:
        card = Card.objects.get(id=request.session.get("card_id"))
        card.lastname    =  request.POST['lastname']
        card.firstname   =  request.POST['firstname']
        card.address     =  request.POST['address']
        card.city        =  request.POST['city']
        card.state       =  request.POST['state']
        card.country     =  request.POST['country']
        card.zipcode     =  request.POST['zipcode']
        card.id_timezone =  request.POST['id_timezone']
        card.phone       =  request.POST['phone']
        card.fax         =  request.POST['fax']
        card.save()
        return HttpResponseRedirect('/')
    if request.method == 'GET' and "card_id" in request.session:
        card = Card.objects.get(id=request.session.get("card_id"))
        form =  CardForm(initial={'lastname': card.lastname,'firstname': 
card.firstname,'address':card.address,'city':card.city,'state':card.state,'country':card.country,'zipcode':card.zipcode,'id_timezone':card.id_timezone,'phone':card.phone,'fax':card.fax})
        return render_to_response('profile_view.html', {'form': form,'card_id':card.id, 'title':'A2Billing | Edit Profile','head':'Welcome, '+ 
card.firstname + ' ' + card.lastname,})
    else:
        logout(request)
        return HttpResponseRedirect('/')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

def check_login(request):
    def errorHandle(error):
		form = LoginForm()
		return render_to_response('login.html', {'error' : error,'form' : form,	})
    if "card_id" in request.session:
        card = Card.objects.get(id=request.session.get("card_id"))
        #card = get_card_detail(request.session.get("card_id"))
        tariff = Tariffgroup.objects.get(id=card.tariff)
        #packageoff = PackageOffer.objects.get(id=tariff.id_cc_package_offer)
        variables = RequestContext(request,
                    {'card_id':card.id,
                     'lastname': card.lastname,
                     'firstname':card.firstname,
                     'email_id':card.email,
                     'phone':card.phone,
                     'fax':card.fax,
                     'address':card.address,
                     'zipcode':card.zipcode,
                     'city':card.city,
                     'state':card.state,
                     'country':card.country,
                     'card_no':card.username,
                     'credit':' %.3f' % card.credit + ' ' + card.currency,
                     'pkg_label':'',
                     'title':'A2Billing | Home',
                     'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
                     'content':''})
        return render_to_response('logged_in.html', variables)#
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                try:
                    username=request.POST['username']
                    password=request.POST['password']

                    card = Card.objects.get(useralias=username)
                    tariff = Tariffgroup.objects.get(id=card.tariff)
                    #packageoff = PackageOffer.objects.get(id=tariff.id_cc_package_offer)

                    if card.uipass == password and card.status == 1:
                        request.session['card_id'] = card.id
                        username = card.username
                        variables = RequestContext(request,
                        {'card_id':card.id,
                         'lastname': card.lastname,
                         'firstname':card.firstname,
                         'email_id':card.email,
                         'phone':card.phone,
                         'fax':card.fax,
                         'address':card.address,
                         'zipcode':card.zipcode,
                         'city':card.city,
                         'state':card.state,
                         'country':card.country,
                         'card_no':card.username,
                         'credit':' %.3f' % card.credit + ' ' + card.currency,
                         'pkg_label':'',
                         'title':'A2Billing | Home',
                         'head':'Welcome, ' + card.firstname + ' ' + card.lastname,
                         'content':''})
                        return render_to_response('logged_in.html',variables)
                    else:                    
                        error = u'invalid login'
                        return errorHandle(error)
                except Card.DoesNotExist:
                    coursestatus = None
                    error = u'User is invalid'
                    return errorHandle(error)
            else:
                error = u'form is invalid'
                return errorHandle(error)
        else:
            form = LoginForm() # An unbound form
            return render_to_response('login.html', {'form': form,})

def logout_view(request):
	logout(request)
	form = LoginForm()
        return HttpResponseRedirect('/')
