from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.auth.models import User


# Create your models here.

#This is used for the queryset in class post

# This is a simple model


# This is a queryset model

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# need to add an import of a reverse
from django.urls import reverse


class Candidate(models.Model):

    objects = None
    # candidate = User
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    candidate_email = models.EmailField()
    candidate_telephone = models.CharField(max_length=10)

    needs_visa =  models.BooleanField(default=False)

    # computer_languages = models.CharField(max_length=100)
    # candidate_http = models.CharField()
    # candidate_content = models.TextField(max_length=100)
    # candidate_resume = models.CharField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # employee = models.CharField(Employee, on_delete = models.CASCADE)

    def __str__(self):
        return self.candidate

    # need to get an absolute url...not sure why???
    def get_absolute_url(self):
        return reverse('candidate-detail', kwargs={'pk': self.pk})

    # queryset based
    #
    # from django.shortcuts import render
    # from .models import Post
    #
    #
    # def index(request):
    #     context = {
    #         'posts': Post.objects.all()
    #     }
    #     return render(request, 'index.html', context)
    #
    #
    # def about(request):
    #     return render(request, 'about.html', {'title': 'About'})
    #

