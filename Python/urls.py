from django.urls import path
from Python.views import *
app_name='Python'
urlpatterns=[
    path('Course/',Course,name='Course'),
    path('Santosh/',Santosh,name='Santosh'),
]