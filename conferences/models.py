import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Conference(models.Model):
    title = models.CharField(max_length=100)
    conference_website = models.CharField(max_length=200)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=datetime)
    updated_at = models.DateTimeField(default=datetime)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.conference_title

    # need to get an absolute url...not sure why???
    def get_absolute_url(self):
        return reverse('conference-detail', kwargs={'pk': self.pk})
