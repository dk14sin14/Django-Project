from django.urls import path
from . import views

'''
Put all the url that belongs to this app in urlpatterns.
Determines which view requests should be executed when request reach those URLs.
'''


# IMPT! DYNAMIC PATH SEGMENTS should be below static paths, otherwise django will treat the link as a dynamic path
urlpatterns = [
    path('meetups/', views.index, name="all-meetups"),
    path('meetups/success', views.confirm_registration, name="confirm_registration"),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name="meetup-details")
]