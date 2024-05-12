from django import template

register = template.Library()

@register.filter
def get_range(value):
    return range(value)


from django import template

register = template.Library()

@register.filter
def first_matching_item(items, condition):
    for item in items:
        if condition(item):
            return item
    return None
