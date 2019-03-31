from django.db import models


class ActiveManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class InactiveManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(active=False)


class PositionalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('position')


class DescPositionalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-position')
