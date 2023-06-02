from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Jsp(request):
    return render(request,'Jsp.html')

def Home(request):
    return HttpResponse('This is home!!!!!!!!!')