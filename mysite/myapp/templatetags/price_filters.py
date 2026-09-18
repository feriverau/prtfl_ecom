from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def clp(value):
    return intcomma(value).replace("\xa0", ".").replace(",", ".")