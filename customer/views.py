# Create your views here.
from django.http import  Http404, HttpResponseRedirect 
from django.template import * 
from django.shortcuts import render_to_response
from django.contrib.auth import logout 
from forms import *
from django.core.mail import send_mail
#from models import *
from django.contrib.auth.models import User
from django.contrib.sessions import *
from datetime import *
from django.core.paginator import *

ITEMS_PER_PAGE = 10

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
        form = CardForm(initial={'lastname': card.lastname,'firstname': 
card.firstname,'address':card.address,'city':card.city,'state':card.state,'country':card.country,'zipcode':card.zipcode,'id_timezone':card.id_timezone,'phone':card.phone,'fax':card.fax})
        return render_to_response('profile_view.html', {'form': form,'card_id':card.id, 'title':'A2Billing | Edit Profile','head':'Welcome, '+ 
card.firstname + ' ' + card.lastname,})
    else:
        logout(request)
        return HttpResponseRedirect('/')

 
def call_detail(request):
    if request.method == 'POST'or request.method == 'GET' and "card_id" in request.session:
        kwargs = {}
        if request.method == 'POST':             
             phone_no        = request.POST['phone_no'].strip()
             phone_no_type   = request.POST['phone_no_type']
             if "fromday_chk" in request.POST:
                 fromday_chk = 'on'
             else:
                 fromday_chk = 'off'
             if "today_chk" in request.POST:
                 today_chk = 'on'
             else:
                 today_chk = 'off'

             call_type       = request.POST['call_type']
             from_day        = int(request.POST['from_day'])
             from_month_year = request.POST['from_month_year']
             from_year       = int(request.POST['from_month_year'][0:4])
             from_month      = int(request.POST['from_month_year'][5:7])
             to_day          = int(request.POST['to_day'])
             to_month_year   = request.POST['to_month_year']
             to_year         = int(request.POST['to_month_year'][0:4])
             to_month        = int(request.POST['to_month_year'][5:7])
             start_date      = datetime(from_year,from_month,from_day)
             end_date        = datetime(to_year,to_month,to_day)
             show            = request.POST['show']
             result          = request.POST['result']
             currency        = request.POST['currency']
             

             if fromday_chk == 'on' and today_chk == 'on':
                 kwargs[ 'starttime__range' ] = (start_date, end_date)
             if fromday_chk == 'on' and today_chk != 'on' :
                 kwargs[ 'starttime__gte' ] = start_date
             if today_chk == 'on' and fromday_chk != 'on':
                 kwargs[ 'starttime__lte' ] = end_date
                 
             if phone_no != '':
                 if phone_no_type == '1':
                     kwargs[ 'calledstation__exact' ] = phone_no
                 if phone_no_type == '2':
                     kwargs[ 'calledstation__startswith' ] = phone_no
                 if phone_no_type == '3':
                     kwargs[ 'calledstation__contains' ] = phone_no
                 if phone_no_type == '4':
                     kwargs[ 'calledstation__endswith' ] = phone_no
             
             if call_type != '' and call_type != '-1':
                 calltype_list = call_type_list()
                 for i in calltype_list:
                     if int(i[0]) == int(call_type) :
                         kwargs[ 'sipiax' ] = call_type
             
             if show == 'ANSWER':
                 kwargs[ 'terminatecauseid__exact' ] = '1'
             if show == 'ALL':
                 list = dial_status_list()
                 kwargs[ 'terminatecauseid__in' ] = (l[0]  for l in list)
             form = 
SearchForm(initial={'fromday_chk':fromday_chk,'from_day':from_day,'from_month_year':from_month_year,'today_chk':today_chk,'to_day':to_day,'to_month_year':to_month_year,'phone_no':phone_no,'phone_no_type':phone_no_type,'call_type':call_type,'currency':currency,'show':show,'result':result})

        if request.method == 'GET':
            form = SearchForm(initial={'currency': config_value('base_currency').upper(),'phone_no_type':1,'show':'ANSWER','result':'min'})
            tday = datetime.today()
            result = 'min'
            kwargs[ 'card_id' ] = request.session.get("card_id")
            kwargs[ 'starttime__gte' ] = datetime(tday.year, tday.month, tday.day)
            currency = config_value('base_currency').upper()
            
        if kwargs:
            card = Card.objects.get(id=request.session.get("card_id"))            
            calls = Call.objects.filter(**kwargs).order_by('-starttime')
            tariffgrp = Tariffgroup.objects.all()
            count = calls.count()
            paginator = Paginator(calls, ITEMS_PER_PAGE)
            try:
                page_number = int(request.REQUEST['page'])
            except (KeyError, ValueError):
                page_number = 1
            try:
                page = paginator.page(page_number)
            except InvalidPage:
                raise Http404
            calls = page.object_list
               
            variables = RequestContext(request,
                        {'form': form,
                         'calls':calls,
                         'count':count,
                         'currency':currency_value(currency),
                         'call_type':call_type_list(),
                         'tariffgrp':tariffgrp,
                         'dial_status':dial_status_list(),
                         'card_id':card.id,
                         'result':result,
                         'title':'A2Billing | Call History',
                         'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
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

   
def check_login(request):
    def errorHandle(error):
		form = LoginForm()
		return render_to_response('login.html', {'error' : error,'form' : form,	})
    if "card_id" in request.session:
        card = Card.objects.get(id=request.session.get("card_id"))
        tariff = Tariffgroup.objects.get(id=card.tariff)
        packageoff = PackageOffer.objects.get(id=tariff.id_cc_package_offer)
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
                     'pkg_label':packageoff.label,
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
                    packageoff = PackageOffer.objects.get(id=tariff.id_cc_package_offer)

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
                         'pkg_label':packageoff.label,
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

