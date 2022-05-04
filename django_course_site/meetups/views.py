from django.shortcuts import render
from django.http import HttpResponse

'''
functions will be invoked automatically by django when we have an incoming request for a certain URL.
'''


def index(request):
    return HttpResponse('Hello world!')