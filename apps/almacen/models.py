from django.db import models
from apps.core.models import UUIDModel
from django.utils.translation import gettext as _


class Almacen(UUIDModel):
    code = models.CharField(_("Código"), max_length=32)
    address = models.CharField(_("Dirección"), max_length=128)
    description = models.TextField(_("Descripción"))


class TipoDocumento(UUIDModel):
    INGRESO = 'IN'
    SALIDA = 'OUT'
    TRANSACTION_TYPES = (
        (INGRESO, _("Ingreso")),
        (SALIDA, _("Salida")),
    )

    transaction_type = models.CharField(_("Tipo de Transacción"), max_length=5,
                                        choices=TRANSACTION_TYPES)