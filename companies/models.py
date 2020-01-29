from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    conference_http = models.CharField()
    conference_content = models.TextField(max_length=100)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,on_delete=modelsCASCADE)


def __str__(self):
    return self.company_name


# need to get an absolute url...not sure why???
def get_absolute_url(self):
    return reverse('company-detail', kwargs={'pk': self.pk})