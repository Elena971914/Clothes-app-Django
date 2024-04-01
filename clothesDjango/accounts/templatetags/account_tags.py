from django import template

register = template.Library()


@register.filter
def placeholder(field, text):
    field.field.widget.attrs['placeholder'] = text
    return field


@register.filter
def add_attribute(field, attribute_and_text):
    attribute, text = attribute_and_text.split(', ', 1)
    field.field.widget.attrs[attribute] = text
    return field
