from django.dispatch import receiver
from django.db.models.signals import post_save

from notifications.signals import notify

from .models import Blog

@receiver(post_save, sender=Blog)
def blog_signal_handler(sender, instance, created, *args, **kwargs):
	notify.send(instance, recipient=instance.author, verb='New blog post', description=instance.title)
