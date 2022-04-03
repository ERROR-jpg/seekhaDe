from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False  )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class posts(models.Model):
    post_id = models.AutoField
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, default="")
    step_title = models.CharField(max_length=10000, blank=True)
    step = models.CharField(max_length=10000, blank=True)
    step_title1 = models.CharField(max_length=10000, blank=True)
    step1 = models.CharField(max_length=10000, blank=True)
    step_title2 = models.CharField(max_length=10000, blank=True)
    step2 = models.CharField(max_length=10000, blank=True)
    step_title3 = models.CharField(max_length=10000, blank=True)
    step3 = models.CharField(max_length=10000, blank=True)
    step_title4 = models.CharField(max_length=10000, blank=True)
    step4 = models.CharField(max_length=10000, blank=True)
    step_title5 = models.CharField(max_length=10000, blank=True)
    step5 = models.CharField(max_length=10000, blank=True)
    step_title6 = models.CharField(max_length=10000, blank=True)
    step6 = models.CharField(max_length=10000, blank=True)
    step_title7 = models.CharField(max_length=10000, blank=True)
    step7 = models.CharField(max_length=10000, blank=True)
    step_title8 = models.CharField(max_length=10000, blank=True)
    step8 = models.CharField(max_length=10000, blank=True)
    step_title9 = models.CharField(max_length=10000, blank=True)
    step9 = models.CharField(max_length=10000, blank=True)

    link = models.CharField(max_length=200, default="")
    thumbnail = models.ImageField(upload_to='posts/images', default="")

    def __str__(self):
       return self.title

