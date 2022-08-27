from django import template

register = template.Library()


@register.filter
def show_exact_length(items_list, fixed_length):
    length = len(list(items_list))
    result = []
    if length > fixed_length:

        for idx in range(0, length, fixed_length):
            result.append(items_list[idx:(idx + fixed_length)])
        return result
    return None
