from django.urls import path

from .views import index_view

app_name = 'common'
urlpatterns = [
    path('', index_view, name='common'),
]
