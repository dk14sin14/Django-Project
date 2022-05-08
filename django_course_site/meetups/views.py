from django.shortcuts import render
from .models import Meetup
from .forms import RegistrationForm

'''
functions will be invoked automatically by django when we have an incoming request for a certain URL.
'''


def index(request):
    meetups = Meetup.objects.all()
    template = render(request, 'meetups/index.html', {'meetups': meetups})
    return template

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        registration_form = RegistrationForm()
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {'meetup_found': False})
        

