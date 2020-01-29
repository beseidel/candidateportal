from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # this user statement below extends the django built in user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')


    # location = models.Charfield(max_length=30)

    # add profile to admin page to register after creating model



    # class FileField(upload_to=None, max_length=100, **options)[source]
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # telephone = models.CharField(User, max_length=10)
    # # computer_languages = models.CharField(max_length=100)
    # website = models.CharField(User, max_length=200)
    # need_visa = models.BooleanField(User, default=False)
    # passed_evaluation = models.BooleanField(User, default=False)

    # social_media= [linkedin = [] , github = [] , facebook = [] , whatsapp = [] , facetime = []


    # training_group = models.ForeignKey(max_length=100)
    # work_status = models.BooleanField(default='False')

    # at_company = models.ForeignKey(max_length=100)
    # vendor = models.ForeignKey(max_length=100)
    # salary = models.ForeignKey(Employee, )
    # social_media = models.ForeignKey(Social, )


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)