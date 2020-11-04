from django.shortcuts import render, get_object_or_404
from .models import Job 

# Create your views here.

def home(request):

    # create a code to get all the jobs from the models
    jobs = Job.objects
    
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk = job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})