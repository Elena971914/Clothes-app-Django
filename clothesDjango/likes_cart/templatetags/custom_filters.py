from django import template

register = template.Library()


@register.filter
def total_price(cart_items):
    total = sum(item.quantity * item.cloth.price for item in cart_items)
    return total
