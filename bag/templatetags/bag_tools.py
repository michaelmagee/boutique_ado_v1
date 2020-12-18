""" Filers and functions """
from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    used in bag html as:
     {{ item.product.price | calc_subtotal:item.quantity }}
    """
    return price * quantity
