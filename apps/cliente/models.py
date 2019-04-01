from django.db import models
from apps.core.models import UUIDModel
from django.utils.translation import gettext as _


class Cliente(UUIDModel):
    document_number = models.CharField(
        _("Número de documento"), max_length=32, unique=True)
    entities = models.ManyToManyField("empresa.Entidad",
                                      related_name="customers",
                                      through="empresa.EntidadCliente",
                                      verbose_name=_("Entidades relacionadas"))