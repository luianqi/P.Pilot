from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.projects.models import Project, Iteration


@receiver(post_save, sender=Project)
def create_iteration(sender, instance, created, **kwargs):
    if created:
        Iteration.objects.create(project=instance)
