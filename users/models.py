from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static

# Create your models here.

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to='avatars/',null=True, blank=True)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.nickname:
            return self.nickname
        else:
            return self.user.username
    
    def image(self):
        if self.avatar:
            return self.avatar
        else:
            return static("images/avatar.svg")