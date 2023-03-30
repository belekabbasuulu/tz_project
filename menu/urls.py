from django.urls import path
from menu.views import my_view

urlpatterns = [
    path('menu/<str:menu_name>/', my_view, name='my_view'),
]