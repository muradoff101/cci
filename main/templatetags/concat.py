from django import template

register = template.Library()

@register.filter(name="concating")
def concating(value, lang):
    return value+"_"+lang