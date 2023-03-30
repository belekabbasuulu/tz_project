from django.shortcuts import render
from menu.templatetags.menu_tags import draw_menu

def my_view(request, menu_name):
    menu_html = draw_menu(context={'request': request}, menu_name=menu_name)
    return render(request, 'my_template.html', {'menu_html': menu_html})