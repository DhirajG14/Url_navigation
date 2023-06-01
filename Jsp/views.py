from django.shortcuts import render

# Create your views here.
def Jsp(request):
    return render(request,'Jsp.html')

def Students(request):
    return render(request,'Students.html')