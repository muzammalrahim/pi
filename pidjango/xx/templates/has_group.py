from django import template
from xx.models import Xuser

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Xuser.objects.filter(email=user.email).first()
    if group is not None:
        if group.role == group_name:
            return True
        else:
            return False
