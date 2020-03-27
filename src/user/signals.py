from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Trainee.objects.create(user=instance)
        Trainer.objects.create(user=instance)
        TraineeAddress.objects.create(user=instance)
        TraineePhy.objects.create(user=instance)
