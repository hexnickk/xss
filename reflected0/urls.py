from django.urls import path

from .views import IndexView

app_name = 'reflected0'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
