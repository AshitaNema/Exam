from django.shortcuts import render
import os
from django.http import HttpResponse

# Create your views here.

def HomePage(request):
    os.system("wssh  --policy=reject")
    return render(request, "Home.html", None)

def Terminal(request):
    
    return render(request, "Terminal.html", None)

def Split(request):
    
    return render(request, "Split.html", None)


def Step3(request):
    
    return render(request, "Step3.html", None)

def Step2(request):
    
    return render(request, "Step2.html", None)

def Step4(request):
    
    return render(request, "Step4.html", None)

def Step5(request):
    
    return render(request, "Step5.html", None)

def Step6(request):
    
    return render(request, "Step6.html", None)