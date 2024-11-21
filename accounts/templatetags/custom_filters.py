from django import template

register = template.Library()

@register.filter
def add_class(value, class_name):
    """Adds a class to the given form field widget."""
    if isinstance(value, str):
        return value
    try:
        value.attrs['class'] = value.attrs.get('class', '') + ' ' + class_name
    except AttributeError:
        pass  # If widget has no 'attrs' (like a string), we just return the value
    return value
