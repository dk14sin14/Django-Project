from django.shortcuts import render

'''
functions will be invoked automatically by django when we have an incoming request for a certain URL.
'''


def index(request):
    return render(request, 'meetups/index.html')
