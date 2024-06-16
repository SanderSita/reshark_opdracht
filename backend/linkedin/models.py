from django.db import models

class Profile(models.Model):
    url = models.CharField(max_length=500)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_function = models.CharField(max_length=255)
    work_experiences = models.ManyToManyField('WorkExperience')
    studies = models.ManyToManyField('Study')
    skills = models.ManyToManyField('Skill')
    connections = models.ManyToManyField('Connection')

class WorkExperience(models.Model):
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)

class Study(models.Model):
    school_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    is_active = models.BooleanField()

class Skill(models.Model):
    name = models.CharField(max_length=255)

class Connection(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
