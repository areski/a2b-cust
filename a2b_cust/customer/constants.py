paid_type_list   = ((0,'PREPAID CARD'),
                    (1,'POSTPAID CARD'))

LANGUAGES = ( ('en', 'English'),
              ('fr', 'French'),
              ('es', 'Spanish'),
              ('br', 'Brazilian'))

card_status_list = ((0,"CANCELLED"),
                    (1,"ACTIVATED"),
                    (2,"NEW"),
                    (3,"WAITING-MAILCONFIRMATION"),
                    (4,"RESERVED"),
                    (5,"EXPIRED"),
                    (6,"SUSPENDED FOR UNDERPAYMENT"),
                    (7,"SUSPENDED FOR LITIGATION"),
                    (8,"WAITING-SUBSCRIPTION-PAYMENT"))

simultaccess_list = ((1,"SIMULTANEOUS ACCESS"),
                     (0,"INDIVIDUAL ACCESS"))

generic_yes_no_list = ((0,'No'),(1,'Yes'))

enableexpire_list = ((0,'NO EXPIRY'),
                     (1,'EXPIRE DATE'),
                     (2,'EXPIRE DAYS SINCE FIRST USE'),
                     (3,'EXPIRE DAYS SINCE CREATION'))

discount_list = []
discount_list.append( ('0.00','NO DISCOUNT') )
for n in range(1,100):
   discount_list.append( (str(n)+".00",str(n)+"%"))


restriction_list = ((0,"NONE RESTRICTION USED"),
                    (1,"CAN'T CALL RESTRICTED NUMBERS"),
                    (2,"CAN ONLY CALL RESTRICTED NUMBERS"))

