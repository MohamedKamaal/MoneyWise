from django.dispatch import receiver
from users.models import User, Profile
from django.db.models.signals import post_save, pre_save

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user
        )

