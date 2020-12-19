import random
from django import template

register = template.Library()

@register.simple_tag
def random_int():
    return 'ra_{0}'.format(random.randint(1000, 99999))