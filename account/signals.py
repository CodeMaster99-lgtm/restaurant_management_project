from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models impoort User
from .models import UserProfile

@receiver (post_save, sender=User)
def creat_or_update_user_profile(sender, instance, created, **kwargs):
         if created:
            UserProfile.objects.create(user=instance)
         else:
            instance.UserProfile.save() 


