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

@register.filter()
def row_counter(value,arg):
    if arg > 1:
        return ((arg-1)*10)+value
    else:
        return value

@register.filter()
def time_in_min(value):
    if value is None:
        value = 0
    min = int(value / 60)
    sec = int(value % 60)
    return str(str(min) + ":" + str(sec))

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
register.filter('row_counter', row_counter)
register.filter('div', div)
register.filter('time_in_min', time_in_min)
register.filter('floatformat2', floatformat2)
register.filter('percent', percent)
