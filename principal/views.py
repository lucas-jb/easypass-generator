from django.shortcuts import render, HttpResponse, redirect
import random
import string

# Create your views here.
def index(request):
    return render(request, "principal/index.html",{})

