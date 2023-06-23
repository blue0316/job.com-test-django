from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    bio = models.TextField()
    about = models.CharField(max_length=255)
    fblink = models.CharField(max_length=255)
    twlink = models.CharField(max_length=255)
    inlink = models.CharField(max_length=255)
    lilink = models.CharField(max_length=255)
    skills = models.JSONField()

class Recruiter(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField()
    cplink = models.CharField(max_length=255)
    fblink = models.CharField(max_length=255)
    twlink = models.CharField(max_length=255)
    inlink = models.CharField(max_length=255)
    lilink = models.CharField(max_length=255)
    skills = models.JSONField()

class JobInfo(models.Model):
    title = models.CharField(max_length=255)
    cpdomain = models.CharField(max_length=255)
    skills = models.JSONField()
    salary = models.BigIntegerField()