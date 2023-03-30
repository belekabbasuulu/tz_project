from django import template
from django.utils.safestring import mark_safe
from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).get_descendants(include_self=True)
    request = context['request']
    current_path = request.path_info
    menu_html = '<ul>'
    for item in menu_items:
        if current_path.startswith(item.url):
            active_class = 'active'
        else:
            active_class = ''
        menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.name}</a></li>'
    menu_html += '</ul>'
    return mark_safe(menu_html)