from django import template
from xx.models import Xuser

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Xuser.objects.filter(role=group_name)
    if group:
        group = group.first()
        return group
    else:
        return False
