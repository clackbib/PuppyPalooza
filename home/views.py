# Create your views here.
from django.shortcuts import render,redirect


def home_page(request):
    return redirect("http://www.google.com")