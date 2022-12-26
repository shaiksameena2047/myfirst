from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h1>this is my first app1 view</h1>')

def sam(request):
    return HttpResponse('<marquee>this my 2nd view in app1</marquee>')