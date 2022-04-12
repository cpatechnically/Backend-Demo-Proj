# https://docs.djangoproject.com/en/3.1/ref/signals/#django.db.models.signals.post_save
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#function, create profile
@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    #if a NEW USER is created (created = true), a new profile will be created
    if created:
        Profile.objects.create(user=instance)
        print('profile created!')


#function, update profile
@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    #if a NEW USER is NOT created (created == False), the existing users profile will be updated
    try:
        instance.profile.save()
        print('profile updated!')
    except:
        print(f"Error on saving profile")
        pass
    try:
        Profile.objects.create(user=instance)
        print('profile created!')
    except:
        print(f"failed to create profile...")
        pass
