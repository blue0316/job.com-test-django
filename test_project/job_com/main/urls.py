from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('candidate', views.Candidate.as_view(), name='candidate'),
    path('recruiters', views.recruiters, name='recruiters'),
    path('job-listings', views.jobListings, name='jobListings'),
]