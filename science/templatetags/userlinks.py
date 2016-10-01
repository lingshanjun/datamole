#coding: utf-8

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(name='userlinks')
def userlinks(value, arg=None):
    creators = value

    all_creators = arg.split('/')
    all_creators = map(lambda x: x.strip(), all_creators)

    for obj in creators:
        if obj.name in all_creators:
            i = all_creators.index(obj.name)
            html = '<a href="/member/%s">%s</a>' % (obj.id, obj.name)
            all_creators[i] = html

    all_creators = ','.join(all_creators)

    return mark_safe(all_creators)

