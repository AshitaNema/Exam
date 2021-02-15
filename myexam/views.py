from django.shortcuts import render
import os
from django.http import HttpResponse

# Create your views here.

def HomePage(request):
    
    return render(request, "Home.html", None)


def Split(request):
    os.system("wssh --fbidhttp=False")
    return render(request, "Split.html", None)


def SuccessPage(request):
    
    return render(request, "Success.html", None)
