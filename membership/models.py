from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from speakers.models import Speaker


class UserDetail(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    speakers = models.ManyToManyField(Speaker)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserDetail.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userdetail.save()

