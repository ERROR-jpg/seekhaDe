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
    steps = models.CharField(max_length=10000)
    link = models.CharField(max_length=200, default="")
    thumbnail = models.ImageField(upload_to='posts/images', default="")

    def __str__(self):
       return self.title

    