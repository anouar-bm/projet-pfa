# custom_filters.py
from django import template

register = template.Library()

@register.filter
def to_range(value):
    try:
        return range(int(value))
    except ValueError:
        return range(0)
