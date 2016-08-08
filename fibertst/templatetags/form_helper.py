from django import template

register = template.Library()

# Move field name to placeholder attribute
@register.filter(name='add_placeholder')
def add_placeholder(field, placeholder = ''):
    if field:
        if field.field.widget.attrs.get('placeholder') is None:
            if placeholder == '':
                placeholder = field.field.label or field.name
            field.field.widget.attrs['placeholder'] = placeholder
    return field