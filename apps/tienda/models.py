from django.db import models
from apps.core.models import UUIDModel
from django.utils.translation import gettext as _


class Tienda(UUIDModel):
    entity = models.ForeignKey(
        "empresa.Entidad", verbose_name=_("Entidad"), on_delete=models.CASCADE)
    code = models.CharField(_("Código"), max_length=32)
    address = models.CharField(_("Dirección"), max_length=128)
    description = models.TextField(_("Descripción"))
