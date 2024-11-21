import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Slider,MenuItem

@receiver(post_delete, sender=Slider)
def delete_image_file(sender, instance, **kwargs):
    """Delete the image file from the filesystem after the model is deleted."""
    if instance.image:
        file_path = instance.image.path
        if os.path.isfile(file_path):
            os.remove(file_path)

@receiver(post_delete, sender=MenuItem)
def delete_image_file(sender, instance, **kwargs):
    """Delete the image file from the filesystem after the model is deleted."""
    if instance.image:
        file_path = instance.image.path
        if os.path.isfile(file_path):
            os.remove(file_path)
