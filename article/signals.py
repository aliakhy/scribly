from django.db.models.signals import pre_save
from django.dispatch import receiver
import os
from django.db.models.signals import post_delete

# models
from .models import Article


@receiver(pre_save, sender=Article)
def delete_old_image(sender, instance, **kwargs):

    if instance.pk:
        try:

            old_image = Article.objects.get(pk=instance.pk).picture
        except Article.DoesNotExist:
            return


        new_image = instance.picture

        if old_image and old_image != new_image:

            if os.path.isfile(old_image.path):
                os.remove(old_image.path)




@receiver(post_delete, sender=Article)
def delete_image_on_delete(sender, instance, **kwargs):

    if instance.picture:

        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)