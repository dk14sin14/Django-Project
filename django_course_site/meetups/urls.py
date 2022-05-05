from django.urls import path
from . import views

'''
Put all the url that belongs to this app in urlpatterns.
Determines which view requests should be executed when request reach those URLs.
'''


urlpatterns = [
    path('meetups/', views.index, name="all-meetups"),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name="meetup-detail")
]