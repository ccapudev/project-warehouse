from django.db import models
from uuid import uuid4
from .managers import (
    ActiveManager, InactiveManager, PositionalManager,
    DescPositionalManager
)
from django.utils.translation import gettext as _


class VisibilityModel(models.Model):
    active = models.BooleanField(_("Activo"), default=True)
    objects_active = ActiveManager()
    objects_inactive = InactiveManager()

    class Meta:
        abstract = True


class PositionModel(models.Model):
    position = models.IntegerField(_("Posición"), default=0)
    objects_asc = PositionalManager()
    objects_desc = DescPositionalManager()

    class Meta:
        abstract = True


class PositionVisibilityModel(VisibilityModel, PositionModel):

    class Meta:
        abstract = True


class BaseModel(models.Model):
    name = models.CharField(_("Nombre"), max_length=128, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class UUIDModel(BaseModel):
    uid = models.UUIDField("UUID", default=uuid4)

    def __str__(self):
        return "{}:{}".format(
            self.name, self.uid  # .hex[:6]
        )

    class Meta:
        abstract = True