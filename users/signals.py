from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from users.models import Profile, User


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user
        )

