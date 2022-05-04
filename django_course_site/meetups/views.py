from django.shortcuts import render

'''
functions will be invoked automatically by django when we have an incoming request for a certain URL.
'''


def index(request):
    meetups = [
        {
        'title': 'A first meetup', 
        'location': 'New York', 
        'slug': 'a-first-meet-up'
        },
        {
        'title': 'A second meetup', 
        'location': 'Paris', 
        'slug': 'a-second-meet-up'
        }
    ]

    return render(request, 'meetups/index.html', {'show_meetups': True, 'meetupsKEY': meetups})
