from django.shortcuts import render
from . import models


def home(request):
    return render(request, "first.html")

def statistic(request):
    return render(request , "statistic.html")