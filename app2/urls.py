from django.urls import path
from app2.views import *
app_name='anthing'

urlpatterns=[
    path('rihana/',rihana,name='rihana'),
]