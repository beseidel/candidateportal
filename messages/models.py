from django.db import models

# Create your models here.

class Messages(models.Model):
message_title = models.CharField(max_length=50)
message_content = models.CharField(max_length=200)

sender_id = models.ForeignKey(User,on_delete=models.CASCADE)
receiver_id = models.ForeignKey(User,on_delete=models.CASCADE)



def __str__(self):
    return self.message_title


# need to get an absolute url...not sure why???
def get_absolute_url(self):
    return reverse('message-detail', kwargs={'pk': self.pk})
