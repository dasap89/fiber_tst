from django import template
from fiber.models import Page

register = template.Library()

@register.simple_tag(takes_context=True)
def get_page(context, url, name=''):
    if name == '':
        name = url

    context[name] = Page.objects.get(url=url)
    return ''


@register.simple_tag(takes_context=True)
def get_child_pages(context, url, name=''):
    if name == '':
        name = url

    context[name] = Page.objects.filter(parent__url=url)
    return ''