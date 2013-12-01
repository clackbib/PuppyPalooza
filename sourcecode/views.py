# Create your views here.
from django.shortcuts import render



def sourcecode(request):
    return render(request, "sourcecode/home.html", locals())