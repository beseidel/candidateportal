# from django.db import models
#
# # Create your models here.
#
# class Employee (models.Model):
#     employeeId = models.CharField(max_length=100)
#     citizenship = models.CharField()
#     employeeFirstName = models.CharField(max_length=100)
#     employeeLastName = models.TextField()
#     has_contract = models.BooleanField(default=False)
#     needs_visa = models.BooleanField(default=False)
#     # vendorCompany= models.ForeignKey(default=False)
#     # employeeCompany = models.ForeignKey(Client,on_delete=models.CASCADE)
#     # employeeImage = models.TextField()
#
#     # author = models.ForeignKey(User, on_delete=models.CASCADE)
#     # senderId = models.ForeignKey(User,on_delete=models.CASCADE)
#     # receiverId=models.ForeignKey()
#     # messagesId=models.ForeignKey()
#     # is_Candidate= models.CharField()
#     # email = models.CharField()
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.employeeId
#
#     # need to get an absolute url...not sure why???
#     def get_absolute_url(self):
#         return reverse('employee-detail', kwargs={'pk': self.pk})
