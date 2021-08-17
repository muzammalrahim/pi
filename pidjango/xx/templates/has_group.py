from django import template
from xx.models import Xuser

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Xuser.objects.filter(email=user.email).first()
    if group is not None:
        if group.role == group_name:
            print("hellllo")
            return True
        else:
            print("sdkdskdjskdjskdj")
            return False
    else:
        return group
