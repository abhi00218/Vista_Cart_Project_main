# accounts/templatetags/menu_filters.py
from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr):
    """Access an object's attribute dynamically."""
    return getattr(obj, attr, None)
