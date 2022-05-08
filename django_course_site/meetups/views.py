from django.shortcuts import render, redirect
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
        selected_meetup = Meetup.objects.get(slug=meetup_slug)      # selected_meetup is a Meetup object. get() gets the correct object based on the slug passed in.
        if request.method == 'GET':
            registration_form = RegistrationForm()
            
        else:
            registration_form = RegistrationForm(request.POST)      # passes in the POST request's fields into RegistrationForm
            if registration_form.is_valid():                        # checks if inputs are valid, built in function
                participant = registration_form.save()
                selected_meetup.participants.add(participant)       # adds the participant created above into the participant attribute in the Meetup object. 
                return redirect('confirm_registration')

        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {'meetup_found': False})
        

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')