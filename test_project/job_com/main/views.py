from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from main.models import Candidate, Recruiter, JobInfo

# Create your views here.
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

class Candidate(View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template('candidate.html')
        return HttpResponse(template.render())
    def post(self, request, *args, **kwargs):
        body = request.POST
        print(body)
        print("test body", body)

def recruiters(request):
    template = loader.get_template('recruiters.html')
    return HttpResponse(template.render())

def jobListings(request):
    template = loader.get_template('job-listings.html')
    return HttpResponse(template.render())