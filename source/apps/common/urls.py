from django.urls import path

from .views import index, create, _list, result

urlpatterns = [
    path('', index),
    path('create/', create),
    path('list/', _list),
    path('result/', result),
]
