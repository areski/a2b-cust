from django import template
from django.template.defaultfilters import *
import operator

register = template.Library()

@register.filter()
def mul(value,arg):
        return value * arg
mul.is_safe = True

@register.filter()
def div(value, arg):
    if arg is None:
        return 0
    elif arg is 0:
        return 0
    else:
        return value / arg

@register.filter()
def subtract(value, arg):
    return value - arg

@register.filter
def adjust_for_pagination(value, page):
    value, page = int(value), int(page)
    adjusted_value = value + ((page - 1) * 10)
    return adjusted_value

@register.filter()
def time_in_min(value,arg):
    if value == None :
        value = 0;
    if arg == 'min':
        min = int(value / 60)
        sec = int(value % 60)
        return str(str(min) + ":" + str(sec))
    else:
        min = int(value / 60)
        min = (min * 60)
        sec = int(value % 60)
        total_sec = min + sec
        return str(total_sec)


@register.filter()
def display_2bill(value,currency):
    try:
        value = float(float(value)/float(currency))
    except:      
        return value
    m = value - int(value)
    if m:
        return '%.3f' % value
    else:
        return '%.3f' % int(value)

"""
    Displays a floating point number as 34.2 (with one decimal place) but only if there's a point to be displayed
"""
@register.filter()
def floatformat2(text):
    try:
        f = float(text)
    except:
        return text
    m = f - int(f)
    if m:
        return '%.3f' % f
    else:
        return '%.3f' % int(f)
floatformat2.is_safe = True


@register.filter()
def percent(value):
    return str(round(value * 100, 2)) + " %"


register.filter('mul', mul)
register.filter('subtract', subtract)
register.filter('adjust_for_pagination', adjust_for_pagination)
register.filter('div', div)
register.filter('time_in_min', time_in_min)
register.filter('display_2bill', display_2bill)
register.filter('floatformat2', floatformat2)
register.filter('percent', percent)
