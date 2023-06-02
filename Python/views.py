from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Course(request):
    return render(request,'Course.html')

def Santosh(request):
    return HttpResponse('This is Python Trainer!!!!!')