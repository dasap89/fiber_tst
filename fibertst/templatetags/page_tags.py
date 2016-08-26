from django import template
from fiber.models import Page
from pinax.comments.models import Comment
from django.contrib.contenttypes.models import ContentType

from django.db.models import Q

register = template.Library()

@register.simple_tag(takes_context=True)
def get_page(context, url, name=''):
    if name == '':
        name = url

    context[name] = Page.objects.get(url=url)
    return ''

@register.simple_tag
def get_root_and_child_comments(object):
    """
    Usage:
        {% get_root_and_child_comments obj as var %}
    """
    
    url = object.url
    
    ids = Page.objects.filter(
        Q(parent__url=url)|Q(url=url),
        ).values('id')
    
    return Comment.objects.filter(
        object_id__in=ids,
        content_type=ContentType.objects.get_for_model(object)
    ).order_by('-submit_date')