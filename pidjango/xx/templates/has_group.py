from django import template

from xx.models import Xuser

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Xuser.objects.get(name=group_name)
    except Xuser.DoesNotExist:
        return False
    return group
