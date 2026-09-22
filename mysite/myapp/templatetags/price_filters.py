from decimal import Decimal
from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def clp(value):
    if value is None:
        return ""

    try:
        value = int(value)
    except (ValueError, TypeError):
        return value
    
    return intcomma(value).replace("\xa0", ".").replace(",", ".")