from django import template

register = template.Library()


def range_filter(value):
    if len(value) > 500:
        return value[:500] + "..."
    return value


register.filter('range_filter', range_filter)