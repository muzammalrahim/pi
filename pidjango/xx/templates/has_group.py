from django import template
from xx.models import Xuser

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Xuser.objects.get(email=user.email)
        if group.role == group_name:
            return True
        else:
            return False
    except Xuser.DoesNotExist:
        return False

    return group
