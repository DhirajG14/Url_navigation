from django.urls import path
from Jsp.views import *
app_name='Jsp'
urlpatterns=[
    path('Jsp/',Jsp,name='Jsp'),
    path('Home/',Home,name='Home')
]