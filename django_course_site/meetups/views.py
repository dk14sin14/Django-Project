from django.shortcuts import render

'''
functions will be invoked automatically by django when we have an incoming request for a certain URL.
'''


def index(request):
    meetups = [
        {
        'title': 'A first meetup', 
        'location': 'New York', 
        'slug': 'a-first-meetup'
        },
        {
        'title': 'A second meetup', 
        'location': 'Paris', 
        'slug': 'a-second-meetup'
        }
    ]

    return render(request, 'meetups/index.html', {'show_meetups': True, 'meetups': meetups})

def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A first meetup',
        'description': 'This is a first meetup!'
        }
    return render(request, 'meetups/meetup-details.html', {
         'meetup_title': selected_meetup['title'],
         'meetup_description': selected_meetup['description']
    })
