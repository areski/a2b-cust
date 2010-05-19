# Create your views here.
from django.http import  Http404, HttpResponseRedirect 
from django.template import * 
from django.shortcuts import render_to_response
from django.contrib.auth import logout 
from customer.forms import *
from django.core.mail import send_mail
from customer.models import *
from django.contrib.auth.models import User
from django.contrib.sessions import *
from datetime import *
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.ipn.signals import payment_was_successful
import sys, string, random
import operator

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
    kwargs = {}
    if request.method == 'GET' and "card_id" in request.session:
        
        if "phone_no" in request.GET:
            phone_no        = request.GET['phone_no'].strip()
            phone_no_type   = request.GET['phone_no_type']
        else:
            phone_no        = ''
            phone_no_type   = ''
        
        if "fromday_chk" in request.GET:
            fromday_chk     = 'on'
            from_day        = int(request.GET['from_day'])
            from_month_year = request.GET['from_month_year']
            from_year       = int(request.GET['from_month_year'][0:4])
            from_month      = int(request.GET['from_month_year'][5:7])
            from_day        = validate_days(from_year,from_month,from_day)
            start_date      = datetime(from_year,from_month,from_day)
        else:
            fromday_chk     = ''
            from_day        = ''
            from_month_year = ''
            from_year       = ''
            from_month      = ''
            from_day        = ''
            start_date      = ''

        if "today_chk" in request.GET:
            today_chk       = 'on'
            to_day          = int(request.GET['to_day'])
            to_month_year   = request.GET['to_month_year']
            to_year         = int(request.GET['to_month_year'][0:4])
            to_month        = int(request.GET['to_month_year'][5:7])
            to_day          = validate_days(to_year,to_month,to_day)
            end_date        = datetime(to_year,to_month,to_day)
        else:
            today_chk       = ''
            to_day          = ''
            to_month_year   = ''
            to_year         = ''
            to_month        = ''
            to_day          = ''
            end_date        = ''

        if "call_type" in request.GET:
            call_type       = request.GET['call_type']
        else:
            call_type       = ''

        if "show" in request.GET:
            show            = request.GET['show']
        else:
            show            = ''

        if "result" in request.GET:
            result          = request.GET['result']
        else:
            result          = ''

        if "currency" in request.GET:
            currency        = request.GET['currency']
        else:
            currency        = ''

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

        form = SearchForm(initial={'fromday_chk':fromday_chk,'from_day':from_day,'from_month_year':from_month_year,'today_chk':today_chk,'to_day':to_day,'to_month_year':to_month_year,'phone_no':phone_no,'phone_no_type':phone_no_type,'call_type':call_type,'currency':currency,'show':show,'result':result})

        if len(kwargs) == 0:
            form = SearchForm(initial={'currency': config_value('base_currency').upper(),'phone_no_type':1,'show':'ANSWER','result':'min'})
            tday = datetime.today()
            result = 'min'
            kwargs[ 'starttime__gte' ] = datetime(tday.year, tday.month, tday.day)
            currency = config_value('base_currency').upper()

        kwargs[ 'card_id' ] = request.session.get("card_id")

        if "page" in request.GET:
            page            = request.GET['page']
        else:
            page            = int('1')
        
        if kwargs:
            card = Card.objects.get(id=request.session.get("card_id"))            
            calls = Call.objects.select_related('prefix__destination', 'destination').filter(**kwargs).order_by('-starttime')
            tariffgrp = Tariffgroup.objects.all()
            count = calls.count()
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
                         'page':page,
                         'title':'A2Billing | Call History',
                         'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
                        })
            return render_to_response('call_detail.html', variables)
    else:
        logout(request)
        return HttpResponseRedirect('/')

  
def checkout_payment(request):
    if "card_id" in request.session:
        card = Card.objects.get(id=request.session.get("card_id"))
        form = CheckoutPaymentForm(initial={'payment_method':'paypal'})
        variables = RequestContext(request,
                    {'form': form,
                     'card_id':card.id,
                     'currency':config_value('base_currency').upper(),
                     'title':'A2Billing | Checkout Payment ',
                     'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
                     'content':'',
                    })
        return render_to_response("checkout_payment.html", variables)
    else:
        form = LoginForm() 
        return render_to_response('login.html', {'form': form,})



def checkout_confirmation(request):
    def errorHandle(error):
		form = CheckoutPaymentForm()
		return render_to_response('checkout_payment.html', {'error' : error,'form' : form,})    
    if "card_id" in request.session:
        if "payment_method" in request.POST:
            card = Card.objects.get(id=request.session.get("card_id"))
            payment_method = request.POST['payment_method']
            amount = int(request.POST['purchase_amount'])
            vat    = str(card.vat) + "%"
            vat_amount = amount*card.vat/100
            total_amt_incl_vat = amount + vat_amount
            
            paypal_dict = {"business": config_value('paypal_subscription_account'),
                           "amount": total_amt_incl_vat,
                           "item_name": config_value('item_name'),
                           "invoice": get_unique_id(),
                           "notify_url": "http://88.208.209.200:443/checkout_ipn_process/",
                           "return_url": "http://88.208.209.200:443/checkout_process/?subscribe=true",
                           "cancel_return": "http://88.208.209.200:443/checkout_process/?subscribe=flase",
                          }
            form = PayPalPaymentsForm(initial=paypal_dict)
            variables = RequestContext(request,
                        {'form': form,
                         'card_id':card.id,
                         'action_url':config_value('paypal_payment_url '),
                         'currency':config_value('base_currency').upper(),
                         'payment_method':payment_method,
                         'amount':amount,
                         'vat':vat,
                         'vat_amount':vat_amount,
                         'total_amt_incl_vat':total_amt_incl_vat,
                         'title':'A2Billing | Checkout Confirmation ',
                         'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
                         'content':'',
                         })
            return render_to_response("checkout_confirmation.html", variables)
        else:
            error = u'Select any one payment method'
            return errorHandle(error)
    else:
        form = LoginForm() # An unbound form
        return render_to_response('login.html', {'form': form,})

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # Undertake some action depending upon `ipn_obj`.
    if ipn_obj.custom == "Upgrade all users!":
        Users.objects.update(paid=True)        
payment_was_successful.connect(show_me_the_money)


def checkout_process(request):            
    if "card_id" in request.session:
        card = Card.objects.get(id=request.session.get("card_id"))
        if request.GET["subscribe"] == 'true':
            status = "Your subscription for an automique refill sucess"
        else:
            status = "Your subscription for an automique refill failed"
        variables = RequestContext(request,
                        {'card_id':card.id,
                         'title':'A2Billing | Checkout Process ',
                         'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
                         'status':status,
                         })
        return render_to_response('checkout_process.html',variables)
    else:
        form = LoginForm() # An unbound form
        return render_to_response('login.html', {'form': form,})



def check_login(request):
    def errorHandle(error):
		form = LoginForm()
		return render_to_response('login.html', {'error' : error,'form' : form,	})
    if "card_id" in request.session:
        card = Card.objects.get(id=request.session.get("card_id"))
        tariff = Tariffgroup.objects.get(id=card.tariff)
        #packageoff = PackageOffer.objects.get(id=tariff.id_cc_package_offer)
        purchase_amount_str = config_value('purchase_amount').replace(":","-")
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
                     #'pkg_label':packageoff.label,
                     'title':'A2Billing | Home',
                     'head':'Welcome, ' + card.firstname + ' ' +card.lastname,
                     'content':'',
                     'purchase_amount_str':purchase_amount_str + ' ' + config_value('base_currency').upper(),})
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
                    purchase_amount_str = config_value('purchase_amount').replace(":","-")

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
                         #'pkg_label':packageoff.label,
                         'title':'A2Billing | Home',
                         'head':'Welcome, ' + card.firstname + ' ' + card.lastname,
                         'content':'',
                         'purchase_amount_str':purchase_amount_str + ' ' + config_value('base_currency').upper(),})
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

