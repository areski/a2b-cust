# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models #, connection, transaction
#from a2b_cust.customer.function_def import *
#from django.forms import ModelForm


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(unique=True)
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type_id = models.IntegerField()
    codename = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    group_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_user_permissions'


class Agent(models.Model):
    id = models.IntegerField(primary_key=True)
    datecreation = models.DateTimeField()
    active = models.CharField(max_length=3)
    login = models.CharField(unique=True, max_length=60)
    passwd = models.CharField(max_length=120, blank=True)
    location = models.TextField(blank=True)
    language = models.CharField(max_length=15, blank=True)
    id_tariffgroup = models.IntegerField(null=True, blank=True)
    options = models.IntegerField()
    credit = models.DecimalField(max_digits=17, decimal_places=5)
    currency = models.CharField(max_length=9, blank=True)
    locale = models.CharField(max_length=30, blank=True)
    commission = models.DecimalField(max_digits=12, decimal_places=4)
    vat = models.DecimalField(max_digits=12, decimal_places=4)
    banner = models.TextField(blank=True)
    perms = models.IntegerField(null=True, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    firstname = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)
    zipcode = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=210, blank=True)
    fax = models.CharField(max_length=60, blank=True)
    company = models.CharField(max_length=150, blank=True)
    com_balance = models.DecimalField(max_digits=17, decimal_places=5)
    threshold_remittance = models.DecimalField(max_digits=17, decimal_places=5)
    bank_info = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_agent'
   
    def __unicode__(self):
        return u'%s %s' % (self.login, self.passwd)

class AgentCommission(models.Model):
    id = models.IntegerField(primary_key=True)
    id_payment = models.IntegerField(null=True, blank=True)
    id_card = models.IntegerField()
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=17, decimal_places=5)
    description = models.TextField(blank=True)
    id_agent = models.IntegerField()
    commission_type = models.IntegerField()
    commission_percent = models.DecimalField(max_digits=12, decimal_places=4)
    class Meta:
        db_table = u'cc_agent_commission'

class AgentSignup(models.Model):
    id = models.IntegerField(primary_key=True)
    id_agent = models.IntegerField()
    code = models.CharField(unique=True, max_length=90)
    id_tariffgroup = models.IntegerField()
    id_group = models.IntegerField()
    class Meta:
        db_table = u'cc_agent_signup'

class AgentTariffgroup(models.Model):
    id_agent = models.IntegerField(primary_key=True)
    id_tariffgroup = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_agent_tariffgroup'

class Alarm(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    periode = models.IntegerField()
    type = models.IntegerField()
    maxvalue = models.FloatField()
    minvalue = models.FloatField()
    id_trunk = models.IntegerField(null=True, blank=True)
    status = models.IntegerField()
    numberofrun = models.IntegerField()
    numberofalarm = models.IntegerField()
    datecreate = models.DateTimeField()
    datelastrun = models.DateTimeField()
    emailreport = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'cc_alarm'

class AlarmReport(models.Model):
    id = models.IntegerField(primary_key=True)
    cc_alarm_id = models.IntegerField()
    calculatedvalue = models.FloatField()
    daterun = models.DateTimeField()
    class Meta:
        db_table = u'cc_alarm_report'

class AutorefillReport(models.Model):
    id = models.IntegerField(primary_key=True)
    daterun = models.DateTimeField()
    totalcardperform = models.IntegerField(null=True, blank=True)
    totalcredit = models.DecimalField(null=True, max_digits=17, decimal_places=5, blank=True)
    class Meta:
        db_table = u'cc_autorefill_report'

class Backup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    path = models.CharField(max_length=765)
    creationdate = models.DateTimeField()
    class Meta:
        db_table = u'cc_backup'

class BillingCustomer(models.Model):
    id = models.IntegerField(primary_key=True)
    id_card = models.IntegerField()
    date = models.DateTimeField()
    id_invoice = models.IntegerField()
    start_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'cc_billing_customer'

class Prefix(models.Model):
    prefix = models.IntegerField(primary_key=True)
    destination = models.CharField(max_length=180)
    class Meta:
        db_table = u'cc_prefix'
        
class Call(models.Model):
    id = models.IntegerField(primary_key=True)
    sessionid = models.CharField(max_length=120)
    uniqueid = models.CharField(max_length=90)
    card_id = models.IntegerField()
    nasipaddress = models.CharField(max_length=90)
    starttime = models.DateTimeField()
    stoptime = models.DateTimeField()
    sessiontime = models.IntegerField(null=True, blank=True)
    calledstation = models.CharField(max_length=90)
    sessionbill = models.FloatField(null=True, blank=True)
    id_tariffgroup = models.IntegerField(null=True, blank=True)
    id_tariffplan = models.IntegerField(null=True, blank=True)
    id_ratecard = models.IntegerField(null=True, blank=True)
    id_trunk = models.IntegerField(null=True, blank=True)
    sipiax = models.IntegerField(null=True, blank=True)
    src = models.CharField(max_length=120)
    id_did = models.IntegerField(null=True, blank=True)
    buycost = models.DecimalField(null=True, max_digits=17, decimal_places=5, blank=True)
    id_card_package_offer = models.IntegerField(null=True, blank=True)
    real_sessiontime = models.IntegerField(null=True, blank=True)
    dnid = models.CharField(max_length=120)
    terminatecauseid = models.IntegerField(null=True, blank=True)
    #destination = models.IntegerField(null=True, blank=True,db_column ="destination")
    destination = models.ForeignKey(Prefix, db_column ="destination", null=True, blank=True)

    def destination_name(self):
        """
        Get the full destination name
        """

        if self.destination is None:
            return ""
        else:
            return self.destination.destination

    class Meta:
        db_table = u'cc_call'


        
class CallArchive(models.Model):
    id = models.IntegerField(primary_key=True)
    sessionid = models.CharField(max_length=120)
    uniqueid = models.CharField(max_length=90)
    card_id = models.IntegerField()
    nasipaddress = models.CharField(max_length=90)
    starttime = models.DateTimeField()
    stoptime = models.DateTimeField()
    sessiontime = models.IntegerField(null=True, blank=True)
    calledstation = models.CharField(max_length=90)
    sessionbill = models.FloatField(null=True, blank=True)
    id_tariffgroup = models.IntegerField(null=True, blank=True)
    id_tariffplan = models.IntegerField(null=True, blank=True)
    id_ratecard = models.IntegerField(null=True, blank=True)
    id_trunk = models.IntegerField(null=True, blank=True)
    sipiax = models.IntegerField(null=True, blank=True)
    src = models.CharField(max_length=120)
    id_did = models.IntegerField(null=True, blank=True)
    buycost = models.DecimalField(null=True, max_digits=17, decimal_places=5, blank=True)
    id_card_package_offer = models.IntegerField(null=True, blank=True)
    real_sessiontime = models.IntegerField(null=True, blank=True)
    dnid = models.CharField(max_length=120)
    terminatecauseid = models.IntegerField(null=True, blank=True)
    destination = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_call_archive'

class CallbackSpool(models.Model):
    id = models.IntegerField(primary_key=True)
    uniqueid = models.CharField(unique=True, max_length=120, blank=True)
    entry_time = models.DateTimeField()
    status = models.CharField(max_length=240, blank=True)
    server_ip = models.CharField(max_length=120, blank=True)
    num_attempt = models.IntegerField()
    last_attempt_time = models.DateTimeField()
    manager_result = models.CharField(max_length=180, blank=True)
    agi_result = models.CharField(max_length=180, blank=True)
    callback_time = models.DateTimeField()
    channel = models.CharField(max_length=180, blank=True)
    exten = models.CharField(max_length=180, blank=True)
    context = models.CharField(max_length=180, blank=True)
    priority = models.CharField(max_length=180, blank=True)
    application = models.CharField(max_length=180, blank=True)
    data = models.CharField(max_length=180, blank=True)
    timeout = models.CharField(max_length=180, blank=True)
    callerid = models.CharField(max_length=180, blank=True)
    variable = models.CharField(max_length=900, blank=True)
    account = models.CharField(max_length=180, blank=True)
    async = models.CharField(max_length=180, blank=True)
    actionid = models.CharField(max_length=180, blank=True)
    id_server = models.IntegerField(null=True, blank=True)
    id_server_group = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_callback_spool'

class Callerid(models.Model):
    id = models.IntegerField(primary_key=True)
    cid = models.CharField(unique=True, max_length=255)
    id_cc_card = models.IntegerField()
    activated = models.CharField(max_length=3)
    class Meta:
        db_table = u'cc_callerid'

class CallplanLcr(models.Model):
    id = models.IntegerField(primary_key=True)
    destination = models.CharField(max_length=180, blank=True)
    dialprefix = models.CharField(max_length=90, blank=True)
    buyrate = models.DecimalField(null=True, max_digits=17, decimal_places=5, blank=True)
    rateinitial = models.DecimalField(null=True, max_digits=17, decimal_places=5, blank=True)
    startdate = models.DateTimeField(null=True, blank=True)
    stopdate = models.DateTimeField(null=True, blank=True)
    initblock = models.IntegerField(null=True, blank=True)
    connectcharge = models.DecimalField(null=True, max_digits=17, decimal_places=5, blank=True)
    id_trunk = models.IntegerField(null=True, blank=True)
    idtariffplan = models.IntegerField(null=True, blank=True)
    ratecard_id = models.IntegerField(null=True, blank=True)
    tariffgroup_id = models.IntegerField()
    class Meta:
        db_table = u'cc_callplan_lcr'

class Campaign(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)
    creationdate = models.DateTimeField()
    startingdate = models.DateTimeField()
    expirationdate = models.DateTimeField()
    description = models.TextField(blank=True)
    id_card = models.IntegerField()
    secondusedreal = models.IntegerField(null=True, blank=True)
    nb_callmade = models.IntegerField(null=True, blank=True)
    status = models.IntegerField()
    frequency = models.IntegerField()
    forward_number = models.CharField(max_length=150, blank=True)
    daily_start_time = models.TextField() # This field type is a guess.
    daily_stop_time = models.TextField() # This field type is a guess.
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()
    id_cid_group = models.IntegerField()
    id_campaign_config = models.IntegerField()
    class Meta:
        db_table = u'cc_campaign'

class CampaignConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    flatrate = models.DecimalField(max_digits=17, decimal_places=5)
    context = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_campaign_config'

class CampaignPhonebook(models.Model):
    id_campaign = models.IntegerField(primary_key=True)
    id_phonebook = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_campaign_phonebook'

class CampaignPhonestatus(models.Model):
    id_phonenumber = models.IntegerField(primary_key=True)
    id_campaign = models.IntegerField(primary_key=True)
    id_callback = models.CharField(max_length=120)
    status = models.IntegerField()
    lastuse = models.DateTimeField()
    class Meta:
        db_table = u'cc_campaign_phonestatus'

class CcCampaignconfCardgroup(models.Model):
    id_campaign_config = models.IntegerField(primary_key=True)
    id_card_group = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_campaignconf_cardgroup'

class Tariffgroup(models.Model):
    id = models.IntegerField(primary_key=True)
    iduser = models.IntegerField()
    idtariffplan = models.IntegerField()
    tariffgroupname = models.CharField(max_length=150)
    lcrtype = models.IntegerField()
    creationdate = models.DateTimeField()
    removeinterprefix = models.IntegerField()
    id_cc_package_offer = models.IntegerField()

    def __unicode__(self):
        return u"%s" % (self.tariffgroupname)
    
    class Meta:
        db_table = u'cc_tariffgroup'

    


class Cardgroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    users_perms = models.IntegerField()
    id_agent = models.IntegerField(null=True, blank=True)
    provisioning = models.CharField(max_length=600, blank=True)

    def __unicode__(self):
        return u"%s" % (self.name)

    class Meta:
        db_table = u'cc_card_group'
        
class Card(models.Model):
    card_status_list = ((0,"CANCELLED"),
                        (1,"ACTIVATED"),
                        (2,"NEW"),
                        (3,"WAITING-MAILCONFIRMATION"),
                        (4,"RESERVED"),
                        (5,"EXPIRED"),
                        (6,"SUSPENDED FOR UNDERPAYMENT"),
                        (7,"SUSPENDED FOR LITIGATION"),
                        (8,"WAITING-SUBSCRIPTION-PAYMENT"))
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    creationdate = models.DateTimeField()
    firstusedate = models.DateTimeField()
    expirationdate = models.DateTimeField()
    enableexpire = models.IntegerField(null=True, blank=True)
    expiredays = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=150, verbose_name='ACCOUNT NUMBER')
    useralias = models.CharField(unique=True, max_length=150, verbose_name='LOGIN')
    uipass = models.CharField(max_length=150)
    credit = models.DecimalField(max_digits=17, decimal_places=5, verbose_name='BA')
    activated = models.CharField(max_length=3)
    status = models.IntegerField(choices=card_status_list, verbose_name='STATUS')#card_status_acronym_list(),
    lastname = models.CharField(max_length=150, verbose_name='LASTNAME')
    firstname = models.CharField(max_length=150, verbose_name='FIRSTNAME')
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    email = models.CharField(max_length=210)
    fax = models.CharField(max_length=60)
    inuse = models.IntegerField(null=True, blank=True)
    simultaccess = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=9, blank=True)
    lastuse = models.DateTimeField()
    nbused = models.IntegerField(null=True, blank=True)
    typepaid = models.IntegerField(null=True, blank=True)
    creditlimit = models.IntegerField(null=True, blank=True)
    voipcall = models.IntegerField(null=True, blank=True)
    sip_buddy = models.IntegerField(null=True, blank=True)
    iax_buddy = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=15, blank=True, verbose_name='LG')
    redial = models.CharField(max_length=150)
    runservice = models.IntegerField(null=True, blank=True)
    nbservice = models.IntegerField(null=True, blank=True)
    id_campaign = models.IntegerField(null=True, blank=True)
    num_trials_done = models.IntegerField(null=True, blank=True)
    vat = models.FloatField()
    servicelastrun = models.DateTimeField()
    initialbalance = models.DecimalField(max_digits=17, decimal_places=5)
    invoiceday = models.IntegerField(null=True, blank=True)
    autorefill = models.IntegerField(null=True, blank=True)
    loginkey = models.CharField(max_length=120)
    mac_addr = models.CharField(max_length=51)
    id_timezone = models.IntegerField(null=True, blank=True)
    tag = models.CharField(max_length=150)
    voicemail_permitted = models.IntegerField()
    voicemail_activated = models.IntegerField()
    last_notification = models.DateTimeField(null=True, blank=True)
    email_notification = models.CharField(max_length=210)
    notify_email = models.IntegerField()
    credit_notification = models.IntegerField()
    id_group = models.IntegerField()
    company_name = models.CharField(max_length=150)
    company_website = models.CharField(max_length=180)
    vat_rn = models.CharField(max_length=120, blank=True)
    traffic = models.IntegerField(null=True, blank=True)
    traffic_target = models.CharField(max_length=900)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    restriction = models.IntegerField()
    id_seria = models.IntegerField(null=True, blank=True)
    serial = models.IntegerField(null=True, blank=True)
    tariff = models.ForeignKey(Tariffgroup, db_column ="tariff", null=True, blank=True, verbose_name='PLAN')
    id_didgroup = models.ForeignKey(Cardgroup, db_column ="id_didgroup", null=True,blank=True, verbose_name='GROUP')

    def card_group_name(self):
        """
        Get the full card group name
        """
        if self.id_didgroup is None:
            return ""
        else:
            return self.id_didgroup.name

    def tariff_name(self):
        """
        Get the full tariff name
        """
        if self.tariff is None:
            return ""
        else:
            return self.tariff.tariffgroupname

    def __unicode__(self):
        return u"%.3f %s" % (self.credit, self.currency)

    class Meta:
        db_table = u'cc_card'



class CardArchive(models.Model):
    id = models.IntegerField(primary_key=True)
    creationdate = models.DateTimeField()
    firstusedate = models.DateTimeField()
    expirationdate = models.DateTimeField()
    enableexpire = models.IntegerField(null=True, blank=True)
    expiredays = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=150)
    useralias = models.CharField(max_length=150)
    uipass = models.CharField(max_length=150, blank=True)
    credit = models.DecimalField(max_digits=17, decimal_places=5)
    tariff = models.IntegerField(null=True, blank=True)
    id_didgroup = models.IntegerField(null=True, blank=True)
    activated = models.CharField(max_length=3)
    status = models.IntegerField(null=True, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    firstname = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)
    zipcode = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=210, blank=True)
    fax = models.CharField(max_length=60, blank=True)
    inuse = models.IntegerField(null=True, blank=True)
    simultaccess = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=9, blank=True)
    lastuse = models.DateTimeField()
    nbused = models.IntegerField(null=True, blank=True)
    typepaid = models.IntegerField(null=True, blank=True)
    creditlimit = models.IntegerField(null=True, blank=True)
    voipcall = models.IntegerField(null=True, blank=True)
    sip_buddy = models.IntegerField(null=True, blank=True)
    iax_buddy = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=15, blank=True)
    redial = models.CharField(max_length=150, blank=True)
    runservice = models.IntegerField(null=True, blank=True)
    nbservice = models.IntegerField(null=True, blank=True)
    id_campaign = models.IntegerField(null=True, blank=True)
    num_trials_done = models.IntegerField(null=True, blank=True)
    vat = models.FloatField()
    servicelastrun = models.DateTimeField()
    initialbalance = models.DecimalField(max_digits=17, decimal_places=5)
    invoiceday = models.IntegerField(null=True, blank=True)
    autorefill = models.IntegerField(null=True, blank=True)
    loginkey = models.CharField(max_length=120, blank=True)
    activatedbyuser = models.CharField(max_length=3)
    id_timezone = models.IntegerField(null=True, blank=True)
    tag = models.CharField(max_length=150, blank=True)
    voicemail_permitted = models.IntegerField()
    voicemail_activated = models.IntegerField()
    last_notification = models.DateTimeField(null=True, blank=True)
    email_notification = models.CharField(max_length=210, blank=True)
    notify_email = models.IntegerField()
    credit_notification = models.IntegerField()
    id_group = models.IntegerField()
    company_name = models.CharField(max_length=150, blank=True)
    company_website = models.CharField(max_length=180, blank=True)
    vat_rn = models.CharField(max_length=120, db_column='VAT_RN', blank=True) # Field name made lowercase.
    traffic = models.IntegerField(null=True, blank=True)
    traffic_target = models.TextField(blank=True)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    restriction = models.IntegerField()
    mac_addr = models.CharField(max_length=51)
    class Meta:
        db_table = u'cc_card_archive'



class CardHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField(null=True, blank=True)
    datecreated = models.DateTimeField()
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_card_history'

class CardPackageOffer(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField()
    id_cc_package_offer = models.IntegerField()
    date_consumption = models.DateTimeField()
    used_secondes = models.IntegerField()
    class Meta:
        db_table = u'cc_card_package_offer'

class CardSeria(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    description = models.TextField(blank=True)
    value = models.IntegerField()
    class Meta:
        db_table = u'cc_card_seria'

class CcCardSubscription(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField(null=True, blank=True)
    id_subscription_fee = models.IntegerField(null=True, blank=True)
    startdate = models.DateTimeField()
    stopdate = models.DateTimeField()
    product_id = models.CharField(max_length=300, blank=True)
    product_name = models.CharField(max_length=300, blank=True)
    paid_status = models.IntegerField()
    last_run = models.DateTimeField()
    next_billing_date = models.DateTimeField()
    limit_pay_date = models.DateTimeField()
    class Meta:
        db_table = u'cc_card_subscription'

class CcCardgroupService(models.Model):
    id_card_group = models.IntegerField(primary_key=True)
    id_service = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_cardgroup_service'

class CcCharge(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField()
    iduser = models.IntegerField()
    creationdate = models.DateTimeField()
    amount = models.FloatField()
    chargetype = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    id_cc_did = models.IntegerField(null=True, blank=True)
    id_cc_card_subscription = models.IntegerField(null=True, blank=True)
    cover_from = models.DateField(null=True, blank=True)
    cover_to = models.DateField(null=True, blank=True)
    charged_status = models.IntegerField()
    invoiced_status = models.IntegerField()
    class Meta:
        db_table = u'cc_charge'

class Config(models.Model):
    id = models.IntegerField(primary_key=True)
    config_title = models.CharField(max_length=300, blank=True)
    config_key = models.CharField(max_length=300, blank=True)
    config_value = models.CharField(max_length=600, blank=True)
    config_description = models.TextField()
    config_valuetype = models.IntegerField()
    config_listvalues = models.CharField(max_length=300, blank=True)
    config_group_title = models.CharField(max_length=192)
    class Meta:
        db_table = u'cc_config'

class CcConfigGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    group_title = models.CharField(unique=True, max_length=192)
    group_description = models.CharField(max_length=765)
    class Meta:
        db_table = u'cc_config_group'

class CcConfiguration(models.Model):
    configuration_id = models.IntegerField(primary_key=True)
    configuration_title = models.CharField(max_length=192)
    configuration_key = models.CharField(max_length=192)
    configuration_value = models.CharField(max_length=765)
    configuration_description = models.CharField(max_length=765)
    configuration_type = models.IntegerField()
    use_function = models.CharField(max_length=765, blank=True)
    set_function = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'cc_configuration'

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    countrycode = models.CharField(max_length=240)
    countryprefix = models.CharField(max_length=240)
    countryname = models.CharField(max_length=240)
    class Meta:
        db_table = u'cc_country'

class Currencies(models.Model):
    id = models.IntegerField(primary_key=True)
    currency = models.CharField(unique=True, max_length=9)
    name = models.CharField(max_length=90)
    value = models.DecimalField(max_digits=13, decimal_places=5)
    lastupdate = models.DateTimeField()
    basecurrency = models.CharField(max_length=9)
    class Meta:
        db_table = u'cc_currencies'

class CcDid(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_didgroup = models.IntegerField()
    id_cc_country = models.IntegerField()
    activated = models.IntegerField()
    reserved = models.IntegerField(null=True, blank=True)
    iduser = models.IntegerField()
    did = models.CharField(unique=True, max_length=150)
    creationdate = models.DateTimeField()
    startingdate = models.DateTimeField()
    expirationdate = models.DateTimeField()
    description = models.TextField(blank=True)
    secondusedreal = models.IntegerField(null=True, blank=True)
    billingtype = models.IntegerField(null=True, blank=True)
    fixrate = models.FloatField()
    connection_charge = models.DecimalField(max_digits=17, decimal_places=5)
    selling_rate = models.DecimalField(max_digits=17, decimal_places=5)
    class Meta:
        db_table = u'cc_did'

class CcDidDestination(models.Model):
    id = models.IntegerField(primary_key=True)
    destination = models.CharField(max_length=360)
    priority = models.IntegerField()
    id_cc_card = models.IntegerField()
    id_cc_did = models.IntegerField()
    creationdate = models.DateTimeField()
    activated = models.IntegerField()
    secondusedreal = models.IntegerField(null=True, blank=True)
    voip_call = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_did_destination'

class CcDidUse(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField(null=True, blank=True)
    id_did = models.IntegerField()
    reservationdate = models.DateTimeField()
    releasedate = models.DateTimeField()
    activated = models.IntegerField(null=True, blank=True)
    month_payed = models.IntegerField(null=True, blank=True)
    reminded = models.IntegerField()
    class Meta:
        db_table = u'cc_did_use'

class CcDidgroup(models.Model):
    id = models.IntegerField(primary_key=True)
    didgroupname = models.CharField(max_length=150)
    creationdate = models.DateTimeField()
    class Meta:
        db_table = u'cc_didgroup'

class CcEpaymentLog(models.Model):
    id = models.IntegerField(primary_key=True)
    cardid = models.IntegerField()
    amount = models.CharField(max_length=150)
    vat = models.FloatField()
    paymentmethod = models.CharField(max_length=150)
    cc_owner = models.CharField(max_length=192, blank=True)
    cc_number = models.CharField(max_length=96, blank=True)
    cc_expires = models.CharField(max_length=21, blank=True)
    creationdate = models.DateTimeField()
    status = models.IntegerField()
    cvv = models.CharField(max_length=12, blank=True)
    credit_card_type = models.CharField(max_length=60, blank=True)
    currency = models.CharField(max_length=12, blank=True)
    transaction_detail = models.TextField(blank=True)
    item_type = models.CharField(max_length=90, blank=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_epayment_log'

class CcEpaymentLogAgent(models.Model):
    id = models.IntegerField(primary_key=True)
    agent_id = models.IntegerField()
    amount = models.CharField(max_length=150)
    vat = models.FloatField()
    paymentmethod = models.CharField(max_length=150)
    cc_owner = models.CharField(max_length=192, blank=True)
    cc_number = models.CharField(max_length=96, blank=True)
    cc_expires = models.CharField(max_length=21, blank=True)
    creationdate = models.DateTimeField()
    status = models.IntegerField()
    cvv = models.CharField(max_length=12, blank=True)
    credit_card_type = models.CharField(max_length=60, blank=True)
    currency = models.CharField(max_length=12, blank=True)
    transaction_detail = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_epayment_log_agent'

class CcIaxBuddies(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField()
    name = models.CharField(max_length=240)
    accountcode = models.CharField(max_length=60)
    regexten = models.CharField(max_length=60)
    amaflags = models.CharField(max_length=21, blank=True)
    callerid = models.CharField(max_length=240)
    context = models.CharField(max_length=240)
    defaultip = models.CharField(max_length=45, db_column='DEFAULTip', blank=True) # Field name made lowercase.
    host = models.CharField(max_length=93)
    language = models.CharField(max_length=6, blank=True)
    permit = models.CharField(max_length=285)
    deny = models.CharField(max_length=285)
    mask = models.CharField(max_length=285)
    port = models.CharField(max_length=15)
    qualify = models.CharField(max_length=21, blank=True)
    secret = models.CharField(max_length=240)
    type = models.CharField(max_length=18)
    username = models.CharField(max_length=240)
    disallow = models.CharField(max_length=300)
    allow = models.CharField(max_length=300)
    regseconds = models.IntegerField()
    ipaddr = models.CharField(max_length=45)
    trunk = models.CharField(max_length=9, blank=True)
    dbsecret = models.CharField(max_length=120)
    regcontext = models.CharField(max_length=120)
    sourceaddress = models.CharField(max_length=60)
    mohinterpret = models.CharField(max_length=60)
    mohsuggest = models.CharField(max_length=60)
    inkeys = models.CharField(max_length=120)
    outkey = models.CharField(max_length=120)
    cid_number = models.CharField(max_length=120)
    sendani = models.CharField(max_length=30)
    fullname = models.CharField(max_length=120)
    auth = models.CharField(max_length=60)
    maxauthreq = models.CharField(max_length=45)
    encryption = models.CharField(max_length=60)
    transfer = models.CharField(max_length=30)
    jitterbuffer = models.CharField(max_length=30)
    forcejitterbuffer = models.CharField(max_length=30)
    codecpriority = models.CharField(max_length=120)
    qualifysmoothing = models.CharField(max_length=30)
    qualifyfreqok = models.CharField(max_length=30)
    qualifyfreqnotok = models.CharField(max_length=30)
    timezone = models.CharField(max_length=60)
    adsi = models.CharField(max_length=30)
    setvar = models.CharField(max_length=600)
    requirecalltoken = models.CharField(max_length=60)
    maxcallnumbers = models.CharField(max_length=30)
    maxcallnumbers_nonvalidated = models.CharField(max_length=30)
    class Meta:
        db_table = u'cc_iax_buddies'

class CcInvoice(models.Model):
    id = models.IntegerField(primary_key=True)
    reference = models.CharField(unique=True, max_length=90, blank=True)
    id_card = models.IntegerField()
    date = models.DateTimeField()
    paid_status = models.IntegerField()
    status = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    class Meta:
        db_table = u'cc_invoice'

class CcInvoiceConf(models.Model):
    id = models.IntegerField(primary_key=True)
    key_val = models.CharField(unique=True, max_length=150)
    value = models.CharField(max_length=150)
    class Meta:
        db_table = u'cc_invoice_conf'

class CcInvoiceItem(models.Model):
    id = models.IntegerField(primary_key=True)
    id_invoice = models.IntegerField()
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=17, decimal_places=5)
    vat = models.DecimalField(decimal_places=2, max_digits=6, db_column='VAT') # Field name made lowercase.
    description = models.TextField()
    id_ext = models.IntegerField(null=True, blank=True)
    type_ext = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'cc_invoice_item'

class CcInvoicePayment(models.Model):
    id_invoice = models.IntegerField(primary_key=True)
    id_payment = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_invoice_payment'

class CcIso639(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(unique=True, max_length=48)
    lname = models.CharField(max_length=48, blank=True)
    charset = models.CharField(max_length=48)
    class Meta:
        db_table = u'cc_iso639'

class CcLogpayment(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    payment = models.DecimalField(max_digits=17, decimal_places=5)
    card_id = models.IntegerField()
    id_logrefill = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    added_refill = models.IntegerField()
    payment_type = models.IntegerField()
    added_commission = models.IntegerField()
    agent_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_logpayment'

class CcLogpaymentAgent(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    payment = models.DecimalField(max_digits=17, decimal_places=5)
    agent_id = models.IntegerField()
    id_logrefill = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    added_refill = models.IntegerField()
    payment_type = models.IntegerField()
    class Meta:
        db_table = u'cc_logpayment_agent'

class CcLogrefill(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    credit = models.DecimalField(max_digits=17, decimal_places=5)
    card_id = models.IntegerField()
    description = models.TextField(blank=True)
    refill_type = models.IntegerField()
    added_invoice = models.IntegerField()
    agent_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_logrefill'

class CcLogrefillAgent(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    credit = models.DecimalField(max_digits=17, decimal_places=5)
    agent_id = models.IntegerField()
    description = models.TextField(blank=True)
    refill_type = models.IntegerField()
    class Meta:
        db_table = u'cc_logrefill_agent'

class CcMessageAgent(models.Model):
    id = models.IntegerField(primary_key=True)
    id_agent = models.IntegerField()
    message = models.TextField(blank=True)
    type = models.IntegerField()
    logo = models.IntegerField()
    order_display = models.IntegerField()
    class Meta:
        db_table = u'cc_message_agent'

class CcMonitor(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=150)
    dial_code = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=750, blank=True)
    text_intro = models.CharField(max_length=750, blank=True)
    query_type = models.IntegerField()
    query = models.CharField(max_length=3000, blank=True)
    result_type = models.IntegerField()
    enable = models.IntegerField()
    class Meta:
        db_table = u'cc_monitor'

class CcNotification(models.Model):
    id = models.IntegerField(primary_key=True)
    key_value = models.CharField(max_length=765, blank=True)
    date = models.DateTimeField()
    priority = models.IntegerField()
    from_type = models.IntegerField()
    from_id = models.IntegerField(null=True, blank=True)
    link_id = models.IntegerField(null=True, blank=True)
    link_type = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'cc_notification'

class CcNotificationAdmin(models.Model):
    id_notification = models.IntegerField(primary_key=True)
    id_admin = models.IntegerField(primary_key=True)
    viewed = models.IntegerField()
    class Meta:
        db_table = u'cc_notification_admin'

class CcOutboundCidGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    creationdate = models.DateTimeField()
    group_name = models.CharField(max_length=210)
    class Meta:
        db_table = u'cc_outbound_cid_group'

class CcOutboundCidList(models.Model):
    id = models.IntegerField(primary_key=True)
    outbound_cid_group = models.IntegerField()
    cid = models.CharField(max_length=300, blank=True)
    activated = models.IntegerField()
    creationdate = models.DateTimeField()
    class Meta:
        db_table = u'cc_outbound_cid_list'

class CcPackageGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_package_group'

class PackageOffer(models.Model):
    id = models.IntegerField(primary_key=True)
    creationdate = models.DateTimeField()
    label = models.CharField(max_length=210)
    packagetype = models.IntegerField()
    billingtype = models.IntegerField()
    startday = models.IntegerField()
    freetimetocall = models.IntegerField()
    class Meta:
        db_table = u'cc_package_offer'

class CcPackageRate(models.Model):
    package_id = models.IntegerField(primary_key=True)
    rate_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_package_rate'

class CcPackgroupPackage(models.Model):
    packagegroup_id = models.IntegerField(primary_key=True)
    package_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_packgroup_package'

class CcPaymentMethods(models.Model):
    id = models.IntegerField(primary_key=True)
    payment_method = models.CharField(max_length=300)
    payment_filename = models.CharField(max_length=600)
    class Meta:
        db_table = u'cc_payment_methods'

class CcPayments(models.Model):
    id = models.IntegerField(primary_key=True)
    customers_id = models.IntegerField()
    customers_name = models.CharField(max_length=600)
    customers_email_address = models.CharField(max_length=288)
    item_name = models.CharField(max_length=381, blank=True)
    item_id = models.CharField(max_length=381, blank=True)
    item_quantity = models.IntegerField()
    payment_method = models.CharField(max_length=96)
    cc_type = models.CharField(max_length=60, blank=True)
    cc_owner = models.CharField(max_length=192, blank=True)
    cc_number = models.CharField(max_length=96, blank=True)
    cc_expires = models.CharField(max_length=12, blank=True)
    orders_status = models.IntegerField()
    orders_amount = models.DecimalField(null=True, max_digits=16, decimal_places=6, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    date_purchased = models.DateTimeField(null=True, blank=True)
    orders_date_finished = models.DateTimeField(null=True, blank=True)
    currency = models.CharField(max_length=9, blank=True)
    currency_value = models.DecimalField(null=True, max_digits=16, decimal_places=6, blank=True)
    class Meta:
        db_table = u'cc_payments'

class CcPaymentsAgent(models.Model):
    id = models.IntegerField(primary_key=True)
    agent_id = models.IntegerField()
    agent_name = models.CharField(max_length=600)
    agent_email_address = models.CharField(max_length=288)
    item_name = models.CharField(max_length=381, blank=True)
    item_id = models.CharField(max_length=381, blank=True)
    item_quantity = models.IntegerField()
    payment_method = models.CharField(max_length=96)
    cc_type = models.CharField(max_length=60, blank=True)
    cc_owner = models.CharField(max_length=192, blank=True)
    cc_number = models.CharField(max_length=96, blank=True)
    cc_expires = models.CharField(max_length=12, blank=True)
    orders_status = models.IntegerField()
    orders_amount = models.DecimalField(null=True, max_digits=16, decimal_places=6, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    date_purchased = models.DateTimeField(null=True, blank=True)
    orders_date_finished = models.DateTimeField(null=True, blank=True)
    currency = models.CharField(max_length=9, blank=True)
    currency_value = models.DecimalField(null=True, max_digits=16, decimal_places=6, blank=True)
    class Meta:
        db_table = u'cc_payments_agent'

class CcPaymentsStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status_id = models.IntegerField()
    status_name = models.CharField(max_length=600)
    class Meta:
        db_table = u'cc_payments_status'

class CcPaypal(models.Model):
    id = models.IntegerField(primary_key=True)
    payer_id = models.CharField(max_length=150, blank=True)
    payment_date = models.CharField(max_length=90, blank=True)
    txn_id = models.CharField(max_length=90, blank=True)
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    payer_email = models.CharField(max_length=165, blank=True)
    payer_status = models.CharField(max_length=90, blank=True)
    payment_type = models.CharField(max_length=90, blank=True)
    memo = models.TextField(blank=True)
    item_name = models.CharField(max_length=210, blank=True)
    item_number = models.CharField(max_length=210, blank=True)
    quantity = models.IntegerField()
    mc_gross = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    mc_fee = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    tax = models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True)
    mc_currency = models.CharField(max_length=9, blank=True)
    address_name = models.CharField(max_length=150)
    address_street = models.CharField(max_length=240)
    address_city = models.CharField(max_length=120)
    address_state = models.CharField(max_length=120)
    address_zip = models.CharField(max_length=60)
    address_country = models.CharField(max_length=90)
    address_status = models.CharField(max_length=90)
    payer_business_name = models.CharField(max_length=120)
    payment_status = models.CharField(max_length=90)
    pending_reason = models.CharField(max_length=150)
    reason_code = models.CharField(max_length=90)
    txn_type = models.CharField(max_length=90)
    class Meta:
        db_table = u'cc_paypal'

class CcPhonebook(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    description = models.TextField(blank=True)
    id_card = models.IntegerField()
    class Meta:
        db_table = u'cc_phonebook'

class CcPhonenumber(models.Model):
    id = models.IntegerField(primary_key=True)
    id_phonebook = models.IntegerField()
    number = models.CharField(max_length=90)
    name = models.CharField(max_length=120, blank=True)
    creationdate = models.DateTimeField()
    status = models.IntegerField()
    info = models.TextField(blank=True)
    amount = models.IntegerField()
    class Meta:
        db_table = u'cc_phonenumber'



class CcProvider(models.Model):
    id = models.IntegerField(primary_key=True)
    provider_name = models.CharField(unique=True, max_length=90)
    creationdate = models.DateTimeField()
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_provider'

class CcRatecard(models.Model):
    id = models.IntegerField(primary_key=True)
    idtariffplan = models.IntegerField()
    dialprefix = models.CharField(max_length=90)
    buyrate = models.DecimalField(max_digits=17, decimal_places=5)
    buyrateinitblock = models.IntegerField()
    buyrateincrement = models.IntegerField()
    rateinitial = models.DecimalField(max_digits=17, decimal_places=5)
    initblock = models.IntegerField()
    billingblock = models.IntegerField()
    connectcharge = models.DecimalField(max_digits=17, decimal_places=5)
    disconnectcharge = models.DecimalField(max_digits=17, decimal_places=5)
    stepchargea = models.DecimalField(max_digits=17, decimal_places=5)
    chargea = models.DecimalField(max_digits=17, decimal_places=5)
    timechargea = models.IntegerField()
    billingblocka = models.IntegerField()
    stepchargeb = models.DecimalField(max_digits=17, decimal_places=5)
    chargeb = models.DecimalField(max_digits=17, decimal_places=5)
    timechargeb = models.IntegerField()
    billingblockb = models.IntegerField()
    stepchargec = models.FloatField()
    chargec = models.FloatField()
    timechargec = models.IntegerField()
    billingblockc = models.IntegerField()
    startdate = models.DateTimeField()
    stopdate = models.DateTimeField()
    starttime = models.IntegerField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)
    id_trunk = models.IntegerField(null=True, blank=True)
    musiconhold = models.CharField(max_length=300)
    id_outbound_cidgroup = models.IntegerField(null=True, blank=True)
    rounding_calltime = models.IntegerField()
    rounding_threshold = models.IntegerField()
    additional_block_charge = models.DecimalField(max_digits=17, decimal_places=5)
    additional_block_charge_time = models.IntegerField()
    tag = models.CharField(max_length=150, blank=True)
    disconnectcharge_after = models.IntegerField()
    is_merged = models.IntegerField(null=True, blank=True)
    additional_grace = models.IntegerField()
    minimal_cost = models.DecimalField(max_digits=17, decimal_places=5)
    announce_time_correction = models.DecimalField(max_digits=7, decimal_places=3)
    destination = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_ratecard'

class CcReceipt(models.Model):
    id = models.IntegerField(primary_key=True)
    id_card = models.IntegerField()
    date = models.DateTimeField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.IntegerField()
    class Meta:
        db_table = u'cc_receipt'

class CcReceiptItem(models.Model):
    id = models.IntegerField(primary_key=True)
    id_receipt = models.IntegerField()
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=17, decimal_places=5)
    description = models.TextField()
    id_ext = models.IntegerField(null=True, blank=True)
    type_ext = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'cc_receipt_item'

class CcRemittanceRequest(models.Model):
    id = models.IntegerField(primary_key=True)
    id_agent = models.IntegerField()
    amount = models.DecimalField(max_digits=17, decimal_places=5)
    type = models.IntegerField()
    date = models.DateTimeField()
    status = models.IntegerField()
    class Meta:
        db_table = u'cc_remittance_request'

class CcRestrictedPhonenumber(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=150)
    id_card = models.IntegerField()
    class Meta:
        db_table = u'cc_restricted_phonenumber'

class CcServerGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=180, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_server_group'

class CcServerManager(models.Model):
    id = models.IntegerField(primary_key=True)
    id_group = models.IntegerField(null=True, blank=True)
    server_ip = models.CharField(max_length=120, blank=True)
    manager_host = models.CharField(max_length=150, blank=True)
    manager_username = models.CharField(max_length=150, blank=True)
    manager_secret = models.CharField(max_length=150, blank=True)
    lasttime_used = models.DateTimeField()
    class Meta:
        db_table = u'cc_server_manager'

class CcService(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    amount = models.FloatField()
    period = models.IntegerField()
    rule = models.IntegerField()
    daynumber = models.IntegerField()
    stopmode = models.IntegerField()
    maxnumbercycle = models.IntegerField()
    status = models.IntegerField()
    numberofrun = models.IntegerField()
    datecreate = models.DateTimeField()
    datelastrun = models.DateTimeField()
    emailreport = models.CharField(max_length=300)
    totalcredit = models.FloatField()
    totalcardperform = models.IntegerField()
    operate_mode = models.IntegerField(null=True, blank=True)
    dialplan = models.IntegerField(null=True, blank=True)
    use_group = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_service'

class CcServiceReport(models.Model):
    id = models.IntegerField(primary_key=True)
    cc_service_id = models.IntegerField()
    daterun = models.DateTimeField()
    totalcardperform = models.IntegerField(null=True, blank=True)
    totalcredit = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'cc_service_report'

class CcSipBuddies(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField()
    name = models.CharField(max_length=240)
    accountcode = models.CharField(max_length=60)
    regexten = models.CharField(max_length=60)
    amaflags = models.CharField(max_length=21, blank=True)
    callgroup = models.CharField(max_length=30, blank=True)
    callerid = models.CharField(max_length=240)
    canreinvite = models.CharField(max_length=60)
    context = models.CharField(max_length=240)
    defaultip = models.CharField(max_length=45, db_column='DEFAULTip', blank=True) # Field name made lowercase.
    dtmfmode = models.CharField(max_length=21)
    fromuser = models.CharField(max_length=240)
    fromdomain = models.CharField(max_length=240)
    host = models.CharField(max_length=93)
    insecure = models.CharField(max_length=60)
    language = models.CharField(max_length=6, blank=True)
    mailbox = models.CharField(max_length=150)
    md5secret = models.CharField(max_length=240)
    nat = models.CharField(max_length=9, blank=True)
    permit = models.CharField(max_length=285)
    deny = models.CharField(max_length=285)
    mask = models.CharField(max_length=285)
    pickupgroup = models.CharField(max_length=30, blank=True)
    port = models.CharField(max_length=15)
    qualify = models.CharField(max_length=21, blank=True)
    restrictcid = models.CharField(max_length=3, blank=True)
    rtptimeout = models.CharField(max_length=9, blank=True)
    rtpholdtimeout = models.CharField(max_length=9, blank=True)
    secret = models.CharField(max_length=240)
    type = models.CharField(max_length=18)
    username = models.CharField(max_length=240)
    disallow = models.CharField(max_length=300)
    allow = models.CharField(max_length=300)
    musiconhold = models.CharField(max_length=300)
    regseconds = models.IntegerField()
    ipaddr = models.CharField(max_length=45)
    cancallforward = models.CharField(max_length=9, blank=True)
    fullcontact = models.CharField(max_length=240)
    setvar = models.CharField(max_length=300)
    regserver = models.CharField(max_length=60, blank=True)
    lastms = models.CharField(max_length=33, blank=True)
    defaultuser = models.CharField(max_length=120)
    auth = models.CharField(max_length=30)
    subscribemwi = models.CharField(max_length=30)
    vmexten = models.CharField(max_length=60)
    cid_number = models.CharField(max_length=120)
    callingpres = models.CharField(max_length=60)
    usereqphone = models.CharField(max_length=30)
    incominglimit = models.CharField(max_length=30)
    subscribecontext = models.CharField(max_length=120)
    musicclass = models.CharField(max_length=60)
    mohsuggest = models.CharField(max_length=60)
    allowtransfer = models.CharField(max_length=60)
    autoframing = models.CharField(max_length=30)
    maxcallbitrate = models.CharField(max_length=45)
    outboundproxy = models.CharField(max_length=120)
    rtpkeepalive = models.CharField(max_length=45)
    class Meta:
        db_table = u'cc_sip_buddies'

class CcSipBuddiesEmpty(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField()
    name = models.CharField(max_length=240)
    accountcode = models.CharField(max_length=60)
    regexten = models.CharField(max_length=60)
    amaflags = models.CharField(max_length=21, blank=True)
    callgroup = models.CharField(max_length=30, blank=True)
    callerid = models.CharField(max_length=240)
    canreinvite = models.CharField(max_length=60)
    context = models.CharField(max_length=240)
    defaultip = models.CharField(max_length=45, db_column='DEFAULTip', blank=True) # Field name made lowercase.
    dtmfmode = models.CharField(max_length=21)
    fromuser = models.CharField(max_length=240)
    fromdomain = models.CharField(max_length=240)
    host = models.CharField(max_length=93)
    insecure = models.CharField(max_length=60)
    language = models.CharField(max_length=6, blank=True)
    mailbox = models.CharField(max_length=150)
    md5secret = models.CharField(max_length=240)
    nat = models.CharField(max_length=9, blank=True)
    permit = models.CharField(max_length=285)
    deny = models.CharField(max_length=285)
    mask = models.CharField(max_length=285)
    pickupgroup = models.CharField(max_length=30, blank=True)
    port = models.CharField(max_length=15)
    qualify = models.CharField(max_length=21, blank=True)
    restrictcid = models.CharField(max_length=3, blank=True)
    rtptimeout = models.CharField(max_length=9, blank=True)
    rtpholdtimeout = models.CharField(max_length=9, blank=True)
    secret = models.CharField(max_length=240)
    type = models.CharField(max_length=18)
    username = models.CharField(max_length=240)
    disallow = models.CharField(max_length=300)
    allow = models.CharField(max_length=300)
    musiconhold = models.CharField(max_length=300)
    regseconds = models.IntegerField()
    ipaddr = models.CharField(max_length=45)
    cancallforward = models.CharField(max_length=9, blank=True)
    fullcontact = models.CharField(max_length=240)
    setvar = models.CharField(max_length=300)
    class Meta:
        db_table = u'cc_sip_buddies_empty'

class CcSpeeddial(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cc_card = models.IntegerField(unique=True)
    phone = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    speeddial = models.IntegerField(unique=True, null=True, blank=True)
    creationdate = models.DateTimeField()
    class Meta:
        db_table = u'cc_speeddial'

class CcStatusLog(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    id_cc_card = models.IntegerField()
    updated_date = models.DateTimeField()
    class Meta:
        db_table = u'cc_status_log'

class CcSubscriptionService(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=600)
    fee = models.FloatField()
    status = models.IntegerField()
    numberofrun = models.IntegerField()
    datecreate = models.DateTimeField()
    datelastrun = models.DateTimeField()
    emailreport = models.CharField(max_length=300)
    totalcredit = models.FloatField()
    totalcardperform = models.IntegerField()
    startdate = models.DateTimeField()
    stopdate = models.DateTimeField()
    class Meta:
        db_table = u'cc_subscription_service'

class CcSubscriptionSignup(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=150)
    id_subscription = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1500, blank=True)
    enable = models.IntegerField()
    id_callplan = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_subscription_signup'

class CcSupport(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=210, blank=True)
    language = models.CharField(max_length=15)
    class Meta:
        db_table = u'cc_support'

class CcSupportComponent(models.Model):
    id = models.IntegerField(primary_key=True)
    id_support = models.IntegerField()
    name = models.CharField(max_length=150)
    activated = models.IntegerField()
    type_user = models.IntegerField()
    class Meta:
        db_table = u'cc_support_component'

class CcSystemLog(models.Model):
    id = models.IntegerField(primary_key=True)
    iduser = models.IntegerField()
    loglevel = models.IntegerField()
    action = models.TextField()
    description = models.TextField(blank=True)
    data = models.TextField(blank=True)
    tablename = models.CharField(max_length=765, blank=True)
    pagename = models.CharField(max_length=765, blank=True)
    ipaddress = models.CharField(max_length=765, blank=True)
    creationdate = models.DateTimeField()
    agent = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_system_log'


class CcTariffgroupPlan(models.Model):
    idtariffgroup = models.IntegerField(primary_key=True)
    idtariffplan = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'cc_tariffgroup_plan'

class CcTariffplan(models.Model):
    id = models.IntegerField(primary_key=True)
    iduser = models.IntegerField(unique=True)
    tariffname = models.CharField(unique=True, max_length=150)
    creationdate = models.DateTimeField()
    startingdate = models.DateTimeField()
    expirationdate = models.DateTimeField()
    description = models.TextField(blank=True)
    id_trunk = models.IntegerField(null=True, blank=True)
    secondusedreal = models.IntegerField(null=True, blank=True)
    secondusedcarrier = models.IntegerField(null=True, blank=True)
    secondusedratecard = models.IntegerField(null=True, blank=True)
    reftariffplan = models.IntegerField(null=True, blank=True)
    idowner = models.IntegerField(null=True, blank=True)
    dnidprefix = models.CharField(max_length=90)
    calleridprefix = models.CharField(max_length=90)
    class Meta:
        db_table = u'cc_tariffplan'

class CcTemplatemail(models.Model):
    id = models.IntegerField(primary_key=True)
    id_language = models.CharField(unique=True, max_length=60)
    mailtype = models.CharField(unique=True, max_length=150, blank=True)
    fromemail = models.CharField(max_length=210, blank=True)
    fromname = models.CharField(max_length=210, blank=True)
    subject = models.CharField(max_length=390, blank=True)
    messagetext = models.TextField(blank=True)
    messagehtml = models.TextField(blank=True)
    class Meta:
        db_table = u'cc_templatemail'

class CcTicket(models.Model):
    id = models.IntegerField(primary_key=True)
    id_component = models.IntegerField()
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    priority = models.IntegerField()
    creationdate = models.DateTimeField()
    creator = models.IntegerField()
    status = models.IntegerField()
    creator_type = models.IntegerField()
    viewed_cust = models.IntegerField()
    viewed_agent = models.IntegerField()
    viewed_admin = models.IntegerField()
    class Meta:
        db_table = u'cc_ticket'

class CcTicketComment(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    id_ticket = models.IntegerField()
    description = models.TextField(blank=True)
    creator = models.IntegerField()
    creator_type = models.IntegerField()
    viewed_cust = models.IntegerField()
    viewed_agent = models.IntegerField()
    viewed_admin = models.IntegerField()
    class Meta:
        db_table = u'cc_ticket_comment'

class Timezone(models.Model):
    id = models.IntegerField(primary_key=True)
    gmtzone = models.CharField(max_length=765, blank=True)
    gmttime = models.CharField(max_length=765, blank=True)
    gmtoffset = models.IntegerField()
    class Meta:
        db_table = u'cc_timezone'

class CcTrunk(models.Model):
    id_trunk = models.IntegerField(primary_key=True)
    trunkcode = models.CharField(max_length=150, blank=True)
    trunkprefix = models.CharField(max_length=60, blank=True)
    providertech = models.CharField(max_length=60)
    providerip = models.CharField(max_length=240)
    removeprefix = models.CharField(max_length=60, blank=True)
    secondusedreal = models.IntegerField(null=True, blank=True)
    secondusedcarrier = models.IntegerField(null=True, blank=True)
    secondusedratecard = models.IntegerField(null=True, blank=True)
    creationdate = models.DateTimeField()
    failover_trunk = models.IntegerField(null=True, blank=True)
    addparameter = models.CharField(max_length=360, blank=True)
    id_provider = models.IntegerField(null=True, blank=True)
    inuse = models.IntegerField(null=True, blank=True)
    maxuse = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    if_max_use = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cc_trunk'

class CcUiAuthen(models.Model):
    userid = models.IntegerField(primary_key=True)
    login = models.CharField(unique=True, max_length=150)
    pwd_encoded = models.CharField(max_length=750)
    groupid = models.IntegerField(null=True, blank=True)
    perms = models.IntegerField(null=True, blank=True)
    confaddcust = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150, blank=True)
    direction = models.CharField(max_length=240, blank=True)
    zipcode = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=90, blank=True)
    fax = models.CharField(max_length=90, blank=True)
    datecreation = models.DateTimeField()
    email = models.CharField(max_length=210, blank=True)
    country = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'cc_ui_authen'

class CcVersion(models.Model):
    version = models.CharField(max_length=90)
    class Meta:
        db_table = u'cc_version'

class CcVoucher(models.Model):
    id = models.IntegerField(primary_key=True)
    creationdate = models.DateTimeField()
    usedate = models.DateTimeField()
    expirationdate = models.DateTimeField()
    voucher = models.CharField(unique=True, max_length=150)
    usedcardnumber = models.CharField(max_length=150, blank=True)
    tag = models.CharField(max_length=150, blank=True)
    credit = models.FloatField()
    activated = models.CharField(max_length=3)
    used = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'cc_voucher'

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=255)
    model = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'
